# -*- coding: utf-8 -*-

import inspect
import json

from flask import request
from marshmallow import Schema
from marshmallow import ValidationError


def process_errors(options, errors):
    custom_error_handler = options.get('schema_error', None)
    if custom_error_handler is not None:
        if isinstance(custom_error_handler, type):
            raise custom_error_handler(errors=errors)

        if isinstance(custom_error_handler, Exception):
            custom_error_handler.errors = errors
            raise custom_error_handler

        if callable(custom_error_handler):
            custom_error_handler(errors=errors)


def injector(function, f_args, f_kwargs, options):

    # Get functions arguments
    function_inspection = inspect.signature(function)

    # Inject schema
    context = None
    if 'schema' in options and 'schema' in function_inspection.parameters:

        # GET DATA
        json_data = {}
        request_method = request.method
        if request_method == 'GET':
            json_data = request.args.copy()
            if 'json' in json_data:
                json_data = json.loads(json_data['json'])

            if not isinstance(json_data, (dict, list)):
                process_errors(options, {'payload': ['Requisição inválida.']})

        json_data.update(f_kwargs)

        # GET SCHEMA
        schema = options.get('schema')
        schema_parameters = {}
        if context is not None:
            schema_parameters['context'] = context
        if not isinstance(schema, Schema):
            schema = schema(**schema_parameters)
        else:
            if context is not None:
                setattr(schema, 'context', context)

        # LOAD DATA ON SCHEMA
        try:
            f_kwargs['schema'] = schema.load(json_data)
        except ValidationError as validation:
            if options.get('schema_validate', True) is True:
                process_errors(options, validation.messages)

    # Inject request method
    if 'request_method' in function_inspection.parameters:
        f_kwargs['request_method'] = request.method

    # Execute function
    return function(*f_args, **f_kwargs)


def inject(**options):
    def decorator(function):
        def wrapper_function(*args, **kwargs):
            return injector(function, args, kwargs, options)
        wrapper_function.__name__ = function.__name__
        wrapper_function.__doc__ = function.__doc__
        return wrapper_function
    return decorator

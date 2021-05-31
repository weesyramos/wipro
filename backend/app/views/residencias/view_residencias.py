# coding: utf-8
from flask import jsonify, request

from backend.app.services.residencias.service_residencias import ServiceResidencias
from backend.helpers.decorators.injector import inject
from backend.helpers.exceptions.exception import AppBadRequest

from .schema import RequestResidenciasSchema


class ViewResidencias:

    def __init__(self, blueprint, prefix=''):
        @blueprint.route(prefix, methods=['GET'])
        @inject(
            schema=RequestResidenciasSchema,
            schema_error=AppBadRequest,
        )

        def list_viva_real(schema):
            return jsonify(ServiceResidencias.list(**schema), 200)
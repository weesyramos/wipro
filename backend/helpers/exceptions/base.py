# coding: utf-8
from flask import jsonify

from backend.helpers.exceptions.core import CoreException


class ApiCoreException(CoreException):

    status_code = 500
    errors = {'server': ['Ocorreu um erro em nossos serviços, por favor tente novamente mais tarde.']}

    __errors_response_key__ = 'message'

    def _translate_all(self, data):
        if isinstance(data, str):
            return data
        elif isinstance(data, (list, tuple)):
            new_list = []
            for el in data:
                new_list.append(self._translate_all(el))
            return new_list
        elif isinstance(data, dict):
            new_dict = {}
            for el in data:
                new_dict[el] = self._translate_all(data[el])
            return new_dict
        else:
            return data

    def serialize(self):
        response = jsonify({})

        errors = getattr(self, 'errors', None)
        if errors is not None:
            if 'force_error' in errors:
                data = {
                    self.__errors_response_key__: self._translate_all(errors['force_error'][0])
                }
            else:
                data = {
                    self.__errors_response_key__: self._translate_all(errors)
                }

            extra = getattr(self, 'extra', None)
            if extra is not None:
                data['extra'] = extra
            response = jsonify(data)

        response.status_code = self.status_code
        return response


class ApiCore404Exception(ApiCoreException):

    status_code = 404
    errors = {'server': ['Resource not found.']}

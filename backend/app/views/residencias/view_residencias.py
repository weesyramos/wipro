# coding: utf-8
from flask import jsonify, request

from backend.app.services.residencias.service_residencias import ServiceResidencias
from backend.helpers.decorators.injector import inject
from backend.helpers.exceptions.exception import AppBadRequest

from .schema import RequestResidenciasSchema, RequestLikeSchema


class ViewResidencias:

    def __init__(self, blueprint, prefix=''):


        @blueprint.route(prefix + '/residencias', methods=['GET'])
        @inject(
            schema=RequestResidenciasSchema,
            schema_error=AppBadRequest,
        )

        def list_residencias(schema):
            return jsonify(ServiceResidencias.list_residencias(**schema), 200)

        @blueprint.route(prefix + '/preco-medio', methods=['GET'])
        @inject(
            schema=RequestResidenciasSchema,
            schema_error=AppBadRequest,
        )

        def list_preco_medio(schema):
            return jsonify(ServiceResidencias.list_preco_medio(**schema), 200)


        @blueprint.route(prefix + '/like', methods=['POST'])
        @inject(
            schema=RequestLikeSchema,
            schema_error=AppBadRequest,
        )

        def like(schema):
            return jsonify(ServiceResidencias.like(**schema), 200)
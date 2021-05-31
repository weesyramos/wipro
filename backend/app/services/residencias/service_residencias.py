from flask import current_app

from backend.app.views.residencias.schema import ResponseResidenciasSchema
from backend.core.models.model_residencias import ModelResidencias

class ServiceResidencias:

    @staticmethod
    def list(**schema):
        # import ipdb; ipdb.set_trace()
        # data = ModelResidencias(
        #     id=1,
        #     username='weslley ramos'
        # )
        # current_app.db.session.add(data)
        # current_app.db.session.commit()
        data1 = ModelResidencias.query.all()

        # return True
        return ResponseResidenciasSchema(many=True).dump(data1)
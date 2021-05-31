from flask import Blueprint

from backend.app.views.residencias.view_residencias import ViewResidencias


# CRIA BLUEPRINT
app_blueprint = Blueprint('app', __name__)


ViewResidencias(app_blueprint, '/residencias')

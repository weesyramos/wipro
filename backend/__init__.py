# coding: utf-8
import traceback

from flask import Flask, request
from flask_migrate import Migrate
from time import strftime


from backend import settings
from backend.core.models.model_residencias import configure as config_db
from backend.helpers.exceptions.exception import AppBadRequest
from backend.helpers.exceptions.base import ApiCoreException, ApiCore404Exception


def create_app():
    # Config APP
    app = Flask(__name__)
    app.config.from_object('backend.settings')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    config_db(app)
    Migrate(app, app.db)

    # tratamentos de exceptions
    @app.errorhandler(ApiCoreException)
    def handle_api_core_exception(exc):
        from flask import current_app

        log = app.logger
        if current_app.config.get('TESTING', True) is False:
            exc_traceback = traceback.format_exc()
            timestamp = strftime('[%Y-%b-%d %H:%M]')
            log.info('%s %s %s %s %s 5xx INTERNAL SERVER ERROR\n%s', timestamp,
                     request.remote_addr, request.method, request.scheme,
                     request.full_path, exc_traceback)
        return exc.serialize()

    @app.errorhandler(AppBadRequest)
    def handle_api_bad_request(exc):
        log = app.logger
        timestamp = strftime('[%Y-%b-%d %H:%M]')

        if settings.TESTING is False:
            # request payload
            log.info('%s %s %s %s %s 400 BAD REQUEST PAYLOAD \n', timestamp,
                     request.remote_addr, request.method, request.get_data().decode(),
                     request.full_path)

        return exc.serialize()

    @app.errorhandler(404)
    def handle_not_found_exception(exc):
        log = app.logger

        timestamp = strftime('[%Y-%b-%d %H:%M]')

        if settings.TESTING is False:
            log.info('%s %s %s %s %s 404 NOT FOUND PAYLOAD \n', timestamp, request.remote_addr,
                     request.method, request.get_data().decode(), request.full_path)

        return ApiCore404Exception().serialize()


    @app.route('/')
    def home():
        return 'OK', 200

    # CRIANDO MODULO BLUEPRINT
    from backend.app.views import app_blueprint
    app.register_blueprint(app_blueprint, url_prefix='/v1/api')


    return app

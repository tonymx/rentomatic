from flask import Flask

from application.rest import room

def register_app_callbacks(app):
    @app.before_request
    def app_before_request():
        print('Calling before_request() for the Flask application...')

    @app.after_request
    def app_after_request(response):
        print('Calling after_request() for the Flask application...')
        return response

    @app.teardown_request
    def app_teardown_request(error=None):
        print('Calling teardown_request() for the Flask application...')

    @app.teardown_appcontext
    def app_teardown_appcontext(error=None):
        print('Calling teardown_appcontext() for the Flask application...')

def create_app(config_name):

    app = Flask(__name__)

    config_module = f"application.config.{config_name.capitalize()}Config"

    app.config.from_object(config_module)

    app.register_blueprint(room.blueprint)

    register_app_callbacks(app) 

    return app
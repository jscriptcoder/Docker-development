import os
from flask import Flask
from .db import db
from .api_routes import api


def create():
    app = Flask(__name__)

    # App configuration
    config_class = os.environ.get('APP_SETTINGS') or 'myapp.config.Config'
    app.config.from_object(config_class)

    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite://'):
        with app.app_context():
            db.create_all()

    app.register_blueprint(api)

    return app

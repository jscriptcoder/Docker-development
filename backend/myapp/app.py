import os
import rq
from flask import Flask
from redis import Redis
from .db import db
from .api_routes import api


def create():
    app = Flask(__name__)
    
    config_class = os.environ.get('APP_SETTINGS') or 'myapp.config.Config'
    app.config.from_object(config_class)

    redis = Redis.from_url(app.config['REDIS_URL'])
    app.task_queue = rq.Queue('myapp-queue', connection=redis)

    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite://'):
        with app.app_context():
            db.create_all()

    app.register_blueprint(api)

    return app

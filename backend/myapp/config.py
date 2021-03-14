import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super secret key!'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'sqlite:///' + os.path.join(basedir, 'myapp.sqlite')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    APP_HOST = os.environ.get('APP_HOST') or 'localhost'
    APP_PORT = os.environ.get('APP_PORT') or '5000'
    
    RUN_DEBUG = True
    LOG_LEVEL = 'DEBUG'
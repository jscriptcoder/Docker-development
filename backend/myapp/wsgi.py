# Will be run by gunicorn

from .app import create as create_app

app = create_app()

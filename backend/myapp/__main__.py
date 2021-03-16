from .app import create as create_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.config['RUN_DEBUG'], 
            host=app.config['APP_HOST'], 
            port=app.config['APP_PORT'])

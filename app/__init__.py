from flask import Flask

app = Flask(__name__)
app.debug = True

def create_app():

    # Register Blueprints
    from app.views.main import main_view
    from app.errors.handlers import error_view

    app.register_blueprint(main_view)
    app.register_blueprint(error_view)

    return app


create_app()



"""Initialize Flask Application."""
from flask import Flask


def create_app():
    """Construct the core application."""
    print(__name__)
    app = Flask(__name__, template_folder="templates")

    with app.app_context():
        from . import routes

        return app

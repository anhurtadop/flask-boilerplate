"""App Initializer"""
import logging
from flask import Flask
from flask_cors import CORS

from .routes.index_routes import index_route

app = Flask(__name__)


def init_app(config):
    """Flask app"""

    # Configuration
    app.config.from_object(config)

    # Enable CORS
    CORS(app,
         resources={r"/*": {"origins": "*"}},
         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         supports_credentials=True,
         allow_headers=["Content-Type", "Authorization"])

    # Configure logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(levelname)s] %(asctime)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
        encoding="utf-8")

    # Register blueprints (client)
    v1_cli = "/api/v1"
    app.register_blueprint(index_route, url_prefix=f"{v1_cli}/index")

    # Return app
    return app

from flask import Flask
from .routes import register_routes
from .utils import db, migrate
from .config import Config

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    register_routes(app)

    with app.app_context():
        # create database tables if they don't exist
        db.create_all()

    return app


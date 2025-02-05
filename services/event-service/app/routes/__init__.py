from flask import Blueprint
from .events import event_blueprint

# register all event blueprints
def register_routes(app):
    app.register_blueprint(event_blueprint, url_prefix="/api")

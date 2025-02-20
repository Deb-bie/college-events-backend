from flask import Blueprint
from .users import user_blueprint

# register all user blueprints
def register_routes(app):
    app.register_blueprint(user_blueprint, url_prefix="/api")

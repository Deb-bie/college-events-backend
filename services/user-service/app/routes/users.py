from flask import Blueprint, request, jsonify
from ..models import User, db


# define the Blueprint
user_blueprint = Blueprint("user", __name__)

# define the routes
@user_blueprint.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    try:
        username = data['username']
        email = data['email']
        password = data['password']

        user = User()
        user.username = username
        user.email = email
        user.password = password

        db.session.add(user)
        db.session.commit()

        return jsonify(
            {
                'message': 'User added',
                'result': user.to_json()
            }
        ), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "Error": str(e)
            }
        ), 400



@user_blueprint.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify(
            {
                "error": "User not found"
            }
        ), 404
    return jsonify(user.to_json())



@user_blueprint.route("/users", methods=["GET"])
def get_users():
    data = []
    for user in User.query.all():
        data.append(user.to_json)
    
    return jsonify(data)



@user_blueprint.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = User.query.get(user_id)

    if not user:
        return jsonify(
            {
                "Error": "User not found"
            }
        ), 404
    try:
        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)
        user.password = data.get("password", user.password)
        db.session.commit()

        return jsonify(
            {
                "Message": "User updated",
                "user": user.to_json()
            }
        )
    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "Error": str(e)
            }
        ), 400


@user_blueprint.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify(
            {
                "Error": "User not found"
            }
        ), 404
    
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify(
            {
                "message": "User deleted successfully"
            }
        )
    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "Error": str(e)    
            }
        ), 400


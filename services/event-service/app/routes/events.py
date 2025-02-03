from flask import Blueprint, request, jsonify
from ..models import Event, db

# define the Blueprint
event_blueprint = Blueprint("event", __name__)


@event_blueprint.route("/events", methods=["POST"])
def create_event():
    data = request.get_json()

    try:
        name = data['name']
        description = data['description']
        location = data['location']
        is_virtual = data['is_virtual']
        date = data['date']
        time = data['time']

        event = Event()
        event.name = name
        event.description = description
        event.location = location
        event.is_virtual = is_virtual
        event.date = date
        event.time = time

        db.session.add(event)
        db.session.commit()

        return jsonify(
            {
                'message': "Event created",
                'result': event.to_json()
            }
        ), 201

    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "Error": str(e)
            }
        ), 400
    



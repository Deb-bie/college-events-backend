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
                "error": str(e)
            }
        ), 400


@event_blueprint.route("/events/<int:event_id>", methods=["GET"])
def get_event(event_id):
    event = Event.query.get(event_id)
    if not event:
        return jsonify(
            {
                "error": "Event not found"
            }
        ), 404
    return jsonify(event.to_json())



@event_blueprint.route("/events", methods=["GET"])
def get_events():
    data = []
    for event in Event.query.all():
        data.append(event.to_json)
    
    return jsonify(data)



@event_blueprint.route("/events/<int:event_id>", methods=["PUT"])
def update_user(event_id):
    data = request.get_json()
    event = Event.query.get(event_id)

    if not event:
        return jsonify(
            {
                "error": "Event not found"
            }
        ), 404
    try:
        event.name = data.get("name", event.name)
        event.description = data.get("description", event.description)
        event.location = data.get("location", event.location)
        event.is_virtual = data.get("is_virtual", event.is_virtual)
        event.date = data.get("date", event.date)
        event.time = data.get("time", event.time)

        db.session.commit()

        return jsonify(
            {
                "message": "Event updated",
                "event": event.to_json()
            }
        )
    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "error": str(e)
            }
        ), 400


@event_blueprint.route("/events/<event_id>", methods=["DELETE"])
def delete_event(event_id):
    event = Event.query.get(event_id)

    if not event:
        return jsonify(
            {
                "error": "Event not found"
            }
        ), 404
    
    try:
        db.session.delete(event)
        db.session.commit()
        return jsonify(
            {
                "message": "Event deleted successfully"
            }
        )
    except Exception as e:
        db.session.rollback()
        return jsonify(
            {
                "error": str(e)    
            }
        ), 400



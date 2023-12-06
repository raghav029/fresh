from flask import Blueprint, jsonify, request, session
from models import UserEvent, UserEvent_schema, Events, events_schema 


from db.database import db

ue = Blueprint("user_events", __name__)

# ****user-events routes****
@ue.route('/apply/event', methods=['POST'])
def apply_user_events():
    user_id = session.get('user_id')
    # check if user exist
    if not user_id:
        return jsonify("Unauthorised asscess"), 401
    
    # get the event id
    event_id = request.json['event_id']

    user_event = UserEvent.query.filter_by(user_id=user_id, event_id=event_id).first()
    if user_event:
        user_event.applied = True
    else:
        user_event = UserEvent(user_id=user_id, event_id=event_id, applied=True,mainlied=True)
        db.session.add(user_event)
    
    db.session.commit()

    return UserEvent_schema.jsonify(user_event)

@ue.route('/get/participant/events')
def get_current_user_events():
    user_id = session.get('user_id')
    # check if user exist
    if not user_id:
        return jsonify("Unauthorised asscess"), 401
    # retrieve all the events user applied for
    user_events = UserEvent.query.filter(UserEvent.user_id == user_id).all()

    if not user_events:
        return jsonify("No events selected")
    
    # retrieve events details for each user_event
    event_ids = [user_event.event_id for user_event in user_events]
    all_events = Events.query.filter(Events.id.in_(event_ids)).all()

    event_data = events_schema.dump(all_events)

    return jsonify(event_data)
# get event ids for the applied events
@ue.route('/get/participant/eventsIds')
def get_current_user_events_ids():
    user_id = session.get('user_id')
    # check if user exist
    if not user_id:
        return jsonify("Unauthorised asscess"), 401
    # retrieve all the events user applied for
    user_events = UserEvent.query.filter(UserEvent.user_id == user_id).all()

    if not user_events:
        return jsonify("No events selected")
    
    # retrieve events details for each user_event
    event_ids = [user_event.event_id for user_event in user_events]
    all_events = Events.query.filter(Events.id.in_(event_ids)).all()
    applied_event_ids = [event.id for event in all_events]

    return jsonify(applied_event_ids)
from flask import Blueprint, jsonify
from models import user_schema, users_schema, UserEvent, User, Events, usersName_schema
# UserClubEvents
eu = Blueprint("events_user", __name__)

@eu.route('/get/eventparticipants/<id>/')
def get_event_applicants(id):
    # get the id of events
    event_id = id
    # check for event
    event = Events.query.filter(Events.id==event_id).first()
    if not event:
        return jsonify("Event doesnt exits"), 401
    #retrive all the users applied for the event
    event_users = UserEvent.query.filter(UserEvent.event_id==event_id).all()
    if not event_users:
        return jsonify("No participants"), 402

    #retrive user details for event_users
    user_ids = [user_event.user_id for user_event in event_users]
    
    all_users = User.query.filter(User.id.in_(user_ids)).all()

    users_data = users_schema.dump(all_users)

    return jsonify(users_data)


@eu.route('/get/eventparticipants/name/<id>/')
def get_event_applicants_name(id):
    # get the id of the event
    event_id = id
    # check for event
    event = Events.query.filter(Events.id==event_id).first()
    if not event:
        return jsonify("Event doesnt exits"), 401
    # retrive all the applicants applied
    event_participants = UserEvent.query.filter(UserEvent.event_id==event_id).all()
    if not event_participants:
        return jsonify("No participants"), 402
    
    #retrive user details for event_users
    user_ids = [user_event.user_id for user_event in event_participants]
    all_users = User.query.filter(User.id.in_(user_ids)).all()

    users_data = usersName_schema.dump(all_users)

    return jsonify(users_data)

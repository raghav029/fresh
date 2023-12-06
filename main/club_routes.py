from flask import Blueprint, jsonify, request
from models import club_schema, clubs_schema, Clubs
from db.database import db

club = Blueprint("club", __name__)

@club.route('/get/clubs')
def get_all_clubs_data():
    clubs = Clubs.query.all()
    
    return jsonify(clubs_schema.dump(clubs))

@club.route('/get/club/<id>/')
def get_club_byId(id):
    # check if club exists
    club = Clubs.query.filter(Clubs.club_id==id).first()
    if not club:
        return jsonify("Club not found"), 404
    
    return club_schema.jsonify((club)), 200

@club.route('/add/club', methods=["POST"])
def add_club():
    # get all details
    name = request.json['name']
    image_uri = request.json['image_uri']
    faculty_coordinator = request.json['faculty_coordinator']
    student_coordinator_1 = request.json['student_coordinator_1']
    student_coordinator_2 = request.json['student_coordinator_2']
    description = request.json['description']
    agenda = request.json['agenda']
    entry_fees = request.json['entry_fees']
    
    try:
        club_data = Clubs(name, image_uri, faculty_coordinator, student_coordinator_1, student_coordinator_2, description, agenda, entry_fees)
        db.session.add(club_data)
        db.session.commit()
    except:
        return jsonify("Club not added"), 401
    
    return club_schema.jsonify((club_data)), 200
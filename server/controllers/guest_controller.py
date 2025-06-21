from flask import Blueprint, jsonify
from server.models.guest import Guest
from server.app import db

guest_bp = Blueprint('guest_db', __name__)

@guest_bp.route('/guests', methods=['GET'])
def list_guests():
    guests = Guest.query.all()
    return jsonify([{'id': g.id, 'name': g.name, 'occupation': g.occupation} for g in guests])

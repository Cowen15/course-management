from flask import Blueprint, jsonify, abort, request
from ..models import Departments, Instructor, db
import hashlib
import secrets

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

bp = Blueprint('instructors', __name__, url_prefix='/instructors')

@bp.route('', methods=['GET'])
def index():
    instructor = Instructor.query.all()
    result = []
    for i in instructor:
        result.append(i.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id:int):
    i = Instructor.query.get_or_404(id)
    return jsonify(i.serialize())

@bp.route('', methods=['POST'])
def create():
    i = Instructor(
        username=request.json['username'],
        password=scramble(request.json['password']),
        first_name=request.json['first_name'],
        last_name=request.json['last_name']
    )

    if 'username' not in request.json or 'password' not in request.json or 'first_name' not in request.json or 'last_name' not in request.json:
        return abort(400)
    if len('username') < 3 or len('password') < 8:
        return abort(400)
    db.session.add(i)
    db.session.commit()
    return jsonify(i.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id:int):
    i = Instructor.query.get_or_404(id)
    try:
        db.session.delete(i)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

@bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id:int):
    i = Instructor.query.get_or_404(id)
    try:
        if 'username' in request.json:
            i.username = request.json['username']
        if 'password' in request.json:
            i.password = request.json['password']
        if 'last_name' in request.json:
            i.last_name = request.json['last_name']
        if 'first_name' in request.json:
            i.first_name = request.json['first_name']
        if 'gender' in request.json:
            i.gender = request.json['gender']
        if 'address' in request.json:
            i.address = request.json['address']

        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
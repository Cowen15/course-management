from flask import Blueprint, jsonify, abort, request
from ..models import Student, db
import hashlib
import secrets

def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()

bp = Blueprint('students', __name__, url_prefix='/students')

@bp.route('', methods=['GET'])
def index():
    students = Student.query.all()
    result = []
    for s in students:
        result.append(s.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id:int):
    s = Student.query.get_or_404(id)
    return jsonify(s.serialize())

@bp.route('', methods=['POST'])
def create():
    s = Student(
        username=request.json['username'],
        password=scramble(request.json['password']),
        first_name=request.json['first_name'],
        last_name=request.json['last_name']
    )
    
    if 'username' not in request.json or 'password' not in request.json or 'first_name' not in request.json or 'last_name' not in request.json:
        return abort(400)

    if len('username') <3 or len('password') < 8:
        return abort(400)
    
    db.session.add(s)
    db.session.commit()
    return jsonify(s.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id:int):
    s = Student.query.get_or_404(id)
    try:
        db.session.delete(s)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

@bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update():
    s = Student.query.get_or_404(id)
    try:
        if 'username' in request.json:
            s.username = request.json['username']
        if 'password' in request.json:
            s.password = request.json['password']
        if 'first_name' in request.json:
            s.first_name = request.json['first_name']
        if 'last_name' in request.json:
            s.last_name = request.json['last_name']
        if 'gender' in request.json:
            s.gener = request.json['gender']
        if 'address' in request.json:
            s.address = request.json['address']

        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
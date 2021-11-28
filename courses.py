from flask import Blueprint, jsonify, abort, request

from ..models import Course, db

bp = Blueprint('courses', __name__, url_prefix='/courses')

@bp.route('', methods=['GET'])
def index():
    courses = Course.query.all()
    result = []
    for c in courses:
        result.append(c.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id:int):
    c = Course.query.get_or_404(id)
    return jsonify(c.serialize())

@bp.route('', methods=['POST'])
def add():
    if 'courses_id' not in request.json:
        return abort(400)

    Course.query.get_or_404(request.json['course_id'])

    c = Course(
        user_id = request.json['user_id'],
        course_id= request.json['course_id']
    )

    db.session.add(c)
    db.session.commit()

    return jsonify(c.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id:int):
    c = Course.query.get_or_404(id)
    try:
        db.session.delete(c)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify (False)


from flask import Blueprint, jsonify, abort, request

from ..models import Departments, db

bp = Blueprint('departments', __name__, url_prefix='/departments')

@bp.route('', methods=['GET'])
def index():
    departments = Departments.query.all()
    result = []
    for d in departments:
        result.append(d.serialize())
    return jsonify(result)

@bp.route('/<int:id>', methods=['GET'])
def show(id:int):
    d = Departments.query.get_or_404(id)
    return jsonify(d.serialize())

@bp.route('', methods=['POST'])
def create():
    if 'id' not in request.json:
        return abort(400)
    
    Departments.query.get_or_404(request.json['id'])

    d = Departments(
        dept_id= request.json['dept_id'],
        name=request.json['name']
    )

    db.session.add(d)
    db.session.commit()

    return jsonify(d.serialize())

@bp.route('/<int:id>', methods=['DELETE'])
def delete(id:int):
    d = Departments.query.get_or_404(id)
    try:
        db.session.delete(d)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
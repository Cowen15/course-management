from flask_sqlalchemy import SQLAlchemy
import datetime

from sqlalchemy.orm import backref

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable = False)
    dob = db.Column(db.String(128), nullable = False)
    gender = db.Column(db.String(128), nullable = False)
    address = db.Column(db.String(128), nullable = False)

    takes = db.relationship('Course', backref='students', cascade="all,delete")

    def __init__(self, username: str, password: str, first_name: str, last_name: str):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

class Instructor(db.Model):
    __tablename__ = 'instructors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable = False)
    dob = db.Column(db.String(128), nullable = False)
    gender = db.Column(db.String(128), nullable = False)
    address = db.Column(db.String(128), nullable = False)

    advises = db.relationship('Student', backref='instructors', cascade="all,delete")
    teaches = db.relationship('Course', backref = 'instructors', cascade="all,delete")

    def __init__(self, username: str, password: str, first_name: str, last_name: str):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

class Departments(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(128), nullable = False)

    employs = db.relationship('Instructor', backref='departments', cascade = "all,delete")
    offers = db.relationship('Course', backref='departments', cascade="all,delete")

    def __init__(self, dept_id: int, name: str):
        self.dept_id = dept_id
        self.name = name

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(128), nullable=False)
    max_capacity = db.Column(db.Integer, nullable=False)

    def __init__(self, course_id: int, course_name: str, max_capacity: int):
        self.course_id = course_id
        self.course_name = course_name
        self.max_capacity = max_capacity

    def serialize(self):
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'max_capacity': self.max_capacity
        }
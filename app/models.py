import uuid
from datetime import datetime
from flask_login import UserMixin
from app import db
from sqlalchemy import func

class User(UserMixin, db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    journals = db.relationship('Journal', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Journal(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=func.now())
    user_id = db.Column(db.String(36), db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Journal {}>'.format(self.body)

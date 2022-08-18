from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    time_start = db.Column(db.DateTime)
    time_end = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<Post %r>' % self.title

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)

    def __repr__(self):
        return '<User %r>' % self.title
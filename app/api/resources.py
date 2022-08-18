from flask import request
from flask_restful import Resource

from app import db
from app.models import Event
from .schemas import events_schema, event_schema

class EventListResource(Resource):
    def get(self):
        events = Event.query.all()
        return events_schema.dump(events)

class EventResource(Resource):

    def get(self, id):
        event = Event.query.filter_by(id=id).first()
        return event_schema.dump(event)

    def post(self, id=None):
        try:
            title = request.form['title']
            description = request.form['description']

            event = Event(title=title, description=description)

            db.session.add(event)
            db.session.commit()
        except Exception as e:
            return {"message": str(e)}, 400
        else:
            return None, 200
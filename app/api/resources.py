from datetime import datetime
from app.util import to_datetime

from flask import request
from flask_restful import Resource

from app import db
from app.models import Event
from .schemas import events_schema, event_schema

class ResourceException(Exception):
    pass

class EventListResource(Resource):

    def get(self):
        events = Event.query.all()
        return events_schema.dump(events)

    def post(self):
        try:

            event = Event(
                title = request.form.get('title'),
                description = request.form.get('description'),
                time_start = to_datetime(request.form.get('time_start'), '%m-%d-%Y %H:%M:%S'),
                time_end = to_datetime(request.form.get('time_end'), '%m-%d-%Y %H:%M:%S'),
            )

            if event.time_end and event.time_start > event.time_end:
                raise ResourceException(f"start time ({event.time_start}) can not be later than end time ({event.time_end})")

            db.session.add(event)
            db.session.commit()
        except Exception as e:
            return {"message": str(e)}, 400
        else:
            return {"id": event.id}, 200

class EventResource(Resource):

    def get(self, id):
        event = Event.query.filter_by(id=id).first()
        return event_schema.dump(event)

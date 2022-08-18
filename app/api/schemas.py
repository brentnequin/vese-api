from app.models import Event

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class EventSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Event
        load_instance = True

events_schema = EventSchema(many=True)
event_schema = EventSchema(many=False)
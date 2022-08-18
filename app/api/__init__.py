from flask_restful import Api

from .resources import EventListResource, EventResource

api = Api()

api.add_resource(EventListResource, '/events')
api.add_resource(EventResource, '/events/<int:id>')
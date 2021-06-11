from masonite.api.resources import Resource
from app.Schedule import Schedule
from app.User import User
from masonite.request import Request
from masonite.auth import Auth

from masonite.api.serializers import JSONSerializer
# from masonite.api.authentication import JWTAuthentication

class ScheduleResource(Resource, JSONSerializer):
    model = Schedule
    methods = ['create', 'index', 'show', 'update', 'delete']

    def delete(self, request: Request, auth: Auth):
        # user = request.user()
       
        # return self.model.find(request.param('id'))
        id_to_delete = self.model.find(request.param('id')).id
        self.model.where('id', '=', id_to_delete ).delete()

        return id_to_delete
    
    def create(self, request: Request):
        id_to_cancel = request.id
        cancel_date = request.cancelled_on
        state = request.state

        self.model.where('id', id_to_cancel).update(service_state=state)
        self.model.where('id', id_to_cancel).update(cancelled_on=cancel_date)

        if state == 'Cancelled':
            return "Appointment Cancelled"
        else:
            return "Appointment Uncancelled"
        
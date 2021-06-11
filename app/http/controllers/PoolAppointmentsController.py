"""A PoolAppointmentsController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.auth import Auth
from masonite.controllers import Controller

from app.Schedule import Schedule
from app.User import User

class PoolAppointmentsController(Controller):
    """PoolAppointmentsController Controller Class."""

    def __init__(self, request: Request):
        """PoolAppointmentsController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, request: Request):
        user = request.user()
        customer_schedules = Schedule.where('schedule_id', user.id).get()
        address = user.address
        return view.render('pool_appointments', {'customer_schedules': customer_schedules, 'address':address})
    
    def logout(self, view: View, request: Request, auth: Auth):
        auth.logout()
        return request.redirect('/')

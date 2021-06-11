"""A CustomerSchedulesController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Schedule import Schedule
from app.User import User


class CustomerSchedulesController(Controller):
    """CustomerSchedulesController Controller Class."""

    def __init__(self, request: Request):
        """CustomerSchedulesController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, request: Request):
        customer_schedules = Schedule.all()
        
        return view.render('dashboard/schedules', {'customer_schedules': customer_schedules})

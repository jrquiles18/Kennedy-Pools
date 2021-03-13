"""A TechniciansController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Technician import Technician


class TechniciansController(Controller):
    """TechniciansController Controller Class."""

    def __init__(self, request: Request):
        """TechniciansController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        techs = Technician.all()
        return view.render('dashboard/technicians', {'techs': techs})

    def logout(self, request: Request):
        request.session.reset()
        return request.redirect('/dashboard')

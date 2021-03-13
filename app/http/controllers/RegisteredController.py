"""A RegisteredController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


class RegisteredController(Controller):
    """RegisteredController Controller Class."""

    def __init__(self, request: Request):
        """RegisteredController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view.render('registered')

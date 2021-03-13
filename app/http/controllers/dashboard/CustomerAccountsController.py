"""A CustomerAccountsController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.User import User


class CustomerAccountsController(Controller):
    """CustomerAccountsController Controller Class."""

    def __init__(self, request: Request):
        """CustomerAccountsController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        customers = User.all()
        return view.render('dashboard/customers', {'customers': customers})

    def logout(self, request: Request):
        request.session.reset()
        return request.redirect('/dashboard')

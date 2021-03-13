"""A AccountController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.auth import Auth



class AccountController(Controller):
    """AccountController Controller Class."""

    def __init__(self, request: Request):
        """AccountController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, request: Request, auth:Auth):
        if not request.user():
            return request.redirect('/login')
        return view.render('account')

    # def logout(self, request: Request, auth: Auth):
    #     auth.logout()
    #     return request.redirect('/')

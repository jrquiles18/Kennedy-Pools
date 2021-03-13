"""A HomeController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.auth import Auth



class HomeController(Controller):
    """HomeController Controller Class."""

    def __init__(self, request: Request):
        """HomeController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view.render('home')

    def logout(self, request: Request, auth: Auth):
        auth.logout()
        request.session.flash('success', 'We will see you next time, Whooooooooo!!!!!!')
        return request.redirect('/')

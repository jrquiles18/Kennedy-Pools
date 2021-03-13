"""A PoolCleaningController Module."""

from masonite.request import Request
from masonite.auth import Auth
from masonite.view import View
from masonite.controllers import Controller


class PoolCleaningController(Controller):
    """PoolCleaningController Controller Class."""

    def __init__(self, request: Request):
        """PoolCleaningController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view.render('pool_cleaning')

    def logout(self, view: View, request: Request, auth: Auth):
        auth.logout()
        return request.redirect('/')

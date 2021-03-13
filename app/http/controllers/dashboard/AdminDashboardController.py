"""A AdminDashboardController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from app.Administrator import Administrator


class AdminDashboardController(Controller):
    """AdminDashboardController Controller Class."""

    def __init__(self, request: Request):
        """AdminDashboardController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, request: Request):
        # request.cookie('key', 'value', encrypt=True)
        # return request.get_cookie('key')
        #return request.session.has('key')
        return view.render('dashboard/admin_dashboard')
        


        # if request.session.has('key'):
        #     return view.render('dashboard/admin_dashboard')
        # else:
        #     return request.redirect('dashboard/dashboard_login')

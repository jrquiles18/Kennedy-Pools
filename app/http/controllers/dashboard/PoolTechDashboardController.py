"""A PoolTechDashboardController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller


class PoolTechDashboardController(Controller):
    """PoolTechDashboardController Controller Class."""

    def __init__(self, request: Request):
        """PoolTechDashboardController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view.render('dashboard/pool_tech_dashboard')

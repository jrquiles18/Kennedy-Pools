"""LogoutUser Middleware."""

from masonite.request import Request
from masonite.auth import Auth
from app.http.controllers import AccountUpdateController


class LogoutUserMiddleware:
    """LogoutUser Middleware."""

    def __init__(self, request: Request, auth: Auth):
        """Inject Any Dependencies From The Service Container.

        Arguments:
            Request {masonite.request.Request} -- The Masonite request object
        """
        self.request = request
        self.auth = auth

    def before(self):
        """Run This Middleware Before The Route Executes."""
        pass

    def after(self):
        """Run This Middleware After The Route Executes."""
        pass

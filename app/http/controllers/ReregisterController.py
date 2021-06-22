"""A ReregisterController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.auth import Auth
from masonite.validation import Validator
from masonite import Mail
from app.User import User


class ReregisterController(Controller):
    """ReregisterController Controller Class."""

    def __init__(self, request: Request):
        """ReregisterController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view.render('reregister')

    def reregister(self, request: Request, validate: Validator ):
        errors = request.validate(
            validate.required(['firstname', 'lastname', 'address', 'email', 'username', 'password', 'cell_phone']),
            validate.email('email'),
            validate.strong(
                'password',
                length=8, special=1, uppercase=1,
                # breach=True checks if the password has been breached before.
                # Requires 'pip install pwnedapi'
                breach=False
            )
        )
        if errors:
            return request.back().with_errors(errors).with_input()
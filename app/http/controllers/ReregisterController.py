"""A ReregisterController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.auth import Auth
from masonite.validation import Validator
from masonite import Mail
from app.User import User

from masonite.helpers import password
from datetime import date

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

    def reregister(self, request: Request, validate: Validator, auth: Auth):
        today_date = date.today()

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

        if request.input('password') != request.input('password_confirm'):
            return request.back().with_errors({'error': ['Passwords do not match.  Please make sure passwords match']})

        User.where('id', request.param('id')).update(firstname=request.input('firstname'))
        User.where('id', request.param('id')).update(lastname=request.input('lastname'))
        User.where('id', request.param('id')).update(address=request.input('address'))
        User.where('id', request.param('id')).update(cell_phone=request.input('cell_phone'))
        User.where('id', request.param('id')).update(email=request.input('email'))
        User.where('id', request.param('id')).update(username=request.input('username'))
        User.where('id', request.param('id')).update(password=password(request.input('password')))
        User.where('id', request.param('id')).update(cancelled='No')
        User.where('id', request.param('id')).update(re_activated='Yes')
        User.where('id', request.param('id')).update(reactivated_on=today_date)

        auth.login(request.input('email'), request.input('password'))

        request.session.flash('success', 'Your account has been reactivated.  Thank you for trusing us again.')

        return request.redirect('/')
        

        

        
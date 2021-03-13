"""A PoolTechController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.validation import Validator
from app.Technician import Technician
from masonite.helpers import password
from masonite.managers import SessionManager


import bcrypt


class PoolTechController(Controller):
    """PoolTechController Controller Class."""

    def __init__(self, request: Request):
        """PoolTechController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, request: Request):
        if request.session.has('key'):
            return request.redirect('/tech/dashboard/')
        else:
            return view.render('dashboard/dashboard_login')
        # return view.render('dashboard/dashboard_login')

    def login(self, request: Request, session: SessionManager, validate: Validator):

        tech = Technician.all()
        tech_emails = Technician.lists('pool_tech_email')

        pool_tech_user = tech.where('pool_tech_email', request.input('email')).first()
        pw = tech.where('password', request.input('password')).first()

        errors = request.validate(
            validate.required(['email', 'password']),
            validate.email('email'),
            validate.strong('password', length=8, special=1, uppercase=1)
        )

        #checks for errors in login inputs and redirects user back to login page.
        if errors:
            return request.back().with_errors(errors).with_input()

        #checks to see if admin enters correct email/password credentials and if no admin account exits and needs to register for one.

        if request.input('email') not in tech_emails:
            if not any(bcrypt.checkpw(bytes(request.input('password'), 'utf-8'), bytes(pw, 'utf-8')) for pw in Technician.lists('password')):
                return request.back().with_errors({'email': ['Credentials not found. Please register as a new pool technician.']})
            else:
                return request.back().with_errors({'email': ['Email is incorrect!']})

        elif pool_tech_user and not bcrypt.checkpw(bytes(request.input('password'), 'utf-8'), bytes(pool_tech_user.password, 'utf-8')):
            return request.back().with_errors({'email': ['Password is incorrect!']})

        else:
            session.driver('cookie').set('key', 'value')
            return request.redirect('/tech/dashboard/')

    def logout(self, request: Request):
        request.session.reset()
        return request.redirect('/dashboard')

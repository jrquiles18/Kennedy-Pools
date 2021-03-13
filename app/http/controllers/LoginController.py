"""A LoginController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.validation import Validator
from masonite.auth import Auth
from app.User import User

import bcrypt


class LoginController(Controller):
    """LoginController Controller Class."""

    def __init__(self, request: Request):
        """LoginController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, request: Request):
        if request.user():
            return request.redirect('/')
        return view.render('login')

    def store(self, request: Request, auth: Auth, validate: Validator):
        user = User.all()

        email = User.lists('email')
        pw = User.lists('password')
    
        errors = request.validate(
            validate.required(['email', 'password']),
            validate.email('email')
        )

        #checks for errors in login inputs and redirects user back to login page.
        if errors:
            return request.back().with_errors(errors).with_input()

        elif request.input('email') not in email and request.input('password') not in pw:
            return request.back().with_errors({
            'email': ["Email and password not found. Please register."]
            })

        #check to see if user already had an account which they may have closed/cancelled and need to register for a new account or reactivate account.
        if auth.login(request.input('email'), request.input('password')) and user.where('email', request.input('email')).where('cancelled', 'Yes'):
            request.session.flash('success', 'This account has been cancelled. Please register a new account.')
            auth.logout()
            return request.redirect('/register')
            # return request.back().with_errors({
            # 'email': ["This account has been cancelled.  Please re-register."]
            # })

        #logins user if no errors and account has not been closed/cancelled before
        elif auth.login(request.input('email'), request.input('password')):
            return request.redirect('/')

        # returns back to login page if email or password are incorrect
        return request.back().with_errors({
            'email': ["Email or password is incorrect"]
        })

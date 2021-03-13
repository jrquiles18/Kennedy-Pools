"""A PasswordController Module."""

from masonite import Mail
from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.auth import Auth
from config.auth import AUTH

from masonite.validation import Validator
from app.User import User
from masonite.helpers import password

import bcrypt
import jwt


class PasswordController(Controller):
    """PasswordController Controller Class."""

    def __init__(self, request: Request):
        """PasswordController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, request: Request):
        return view.render('password')

    def forgot(self, view: View, request: Request):
        return view.render('forgot')

    def link(self, view: View):
        return view.render('reset')

    def update(self, view: View, request: Request, auth: Auth, validate: Validator):
        user = User.all()
        pws = User.lists('password')

        customer = request.user()
        pw = customer.password

        if bcrypt.checkpw(bytes(request.input('password'), 'utf-8'), bytes(pw, 'utf-8')) == False:
            return request.back().with_errors({'error': ['Please enter correct old password']})

        new_password = request.input('new_password')
        confirm_password = request.input('confirm_password')

        for pws in pws:
            if bcrypt.checkpw(bytes(request.input('new_password'), 'utf-8'), bytes(pws, 'utf-8')):
                return request.back().with_errors({'error': ['Password already exists.  Please create a new password.']})

        errors = request.validate(
            validate.required(['password', 'new_password', 'confirm_password']),
            validate.strong('new_password',length=8, special=1, uppercase=1,breach=False)
                # breach=True checks if the password has been breached before.
                # Requires 'pip install pwnedapi'
        )

        if errors:
            return request.back().with_errors(errors).with_input()
        elif new_password != confirm_password:
            return request.back().with_errors({'error': ['New password and confirm new password do not match!']})
        else:
            user.where('id', customer.id).first().update(password=password(new_password))
            request.session.flash('success', 'Your password has been successfully updated.')
            return request.redirect('account')

    def send(self, view: View, request: Request, auth: Auth, validate: Validator , mail: Mail):
        email_list = User.lists('email')
        email = request.input('email')
        encoded_jwt = jwt.encode({'email': email, 'httpMethod': 'GET'}, 'secret', algorithm='HS256', ).decode('utf-8')

        errors = request.validate(
            validate.required('email'),
            validate.email('email'))

        if errors:
            return request.back().with_errors(errors)

        if email not in email_list:
            return request.back().with_errors({'error': ['We can not find your email.  Please enter correct email']})

        else:
            message = 'Please visit {}/password/reset/get/{} to reset your password'.format(env('APP_URL', 'http://localhost:8000'), encoded_jwt)
            mail.subject('Reset Password Instructions').to(email).send(message)
            request.session.flash('success', 'An email has been sent. Please follow the instructions in the email to reset your password.')
            return request.redirect('login'), email

    def reset(self, view: View, request: Request, validate: Validator,):
        new_password = request.input('new_password')
        pws = User.lists('password')
        decoded_token = jwt.decode(request.param('id'), 'secret', algorithm='HS256')
        user_email =  decoded_token['email']

        for pw in pws:
            if bcrypt.checkpw(bytes(request.input('new_password'), 'utf-8'), bytes(pw, 'utf-8')):
                return request.back().with_errors({'error': ['Password already exists.  Please create a new password.']})

        errors = request.validate(
            validate.required('new_password'),
            validate.strong('new_password',length=8, special=1, uppercase=1,breach=False)) # breach=True checks if the password has been breached before.
                                                                                          # Requires 'pip install pwnedapi'
        if errors:
            return request.back().with_errors(errors).with_input()
        else:
            AUTH['guards']['web']['model'].where('email', user_email).first().update(password=password(new_password))
            request.session.flash('success', 'Your password has been successfully updated.')
            return request.redirect('login')

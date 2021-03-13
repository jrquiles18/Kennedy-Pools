"""A AdminSetupController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.auth import Auth
from masonite.validation import Validator
from masonite.helpers import password
from masonite.helpers import password
from masonite import env

from app.Administrator import Administrator

import bcrypt
import jwt
import os

class AdminSetupController(Controller):
    """AdminSetupController Controller Class."""

    def __init__(self, request: Request):
        """AdminSetupController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view.render('dashboard/admin_account_setup')

    def register(self, request: Request, auth: Auth, validate: Validator):

        """ register a new administrator and also checks that form is filled out properly without errors and checks to see if email, passwords, and
        usernames alread exits"""

        email = Administrator.lists('admin_email')
        user_name = Administrator.lists('admin_username')
        pw = Administrator.lists('password')

        #check to see if emails or usernames already exist
        accounts = [email, user_name]
        inputs = [request.input('admin_email'), request.input('admin_username')]

        for input in inputs:
            for account in accounts:
                if inputs[0] in accounts[0] and inputs[1] in accounts[1]:
                    return request.back().with_errors({'error': ['{} and {} already exists'.format(inputs[0], inputs[1])]})
                elif input in account:
                    return request.back().with_errors({'error': ['{} already exists'.format(input)]})

        #checking to see if password already exists

        for pw in pw:
            if bcrypt.checkpw(bytes(request.input('admin_password'), 'utf-8'), bytes(pw, 'utf-8')):
                return request.back().with_errors({'error': ['Password already exists.  Please create a new password.']})

        #checking for user entry errors when registering as an Administrator
        errors = request.validate(
            validate.required(['admin_name', 'admin_cell_phone', 'admin_address', 'admin_email', 'admin_username', 'admin_password']),
            validate.email('admin_email'),
            validate.strong('admin_password', length=8, special=1, uppercase=1)
            )

        if errors:
            return request.back().with_errors(errors).with_input()
        #when everything above checks out ok, then go ahead and insert data in Administrator table
        else:
            encoded_jwt = jwt.encode({'email': request.input('admin_email')},os.getenv('KEY') ,algorithm='HS256')
            encrypted_password = password(request.input('admin_password'))
            Administrator.insert(admin_name=request.input('admin_name'),
                                    admin_cell_phone=request.input('admin_cell_phone'),
                                    admin_address=request.input('admin_address'),
                                    admin_email=request.input('admin_email'),
                                    admin_username=request.input('admin_username'),
                                    password=encrypted_password,
                                    remember_token=encoded_jwt)

        return request.redirect('/admin')

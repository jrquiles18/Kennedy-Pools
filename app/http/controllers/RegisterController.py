"""A RegisterController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.auth import Auth
from masonite.validation import Validator
from masonite import Mail
from app.User import User

import bcrypt

class RegisterController(Controller):
    """RegisterController Controller Class."""

    def __init__(self, request: Request):
        """RegisterController Initializer
        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view.render('register')

    def register(self, request: Request, auth: Auth, validate: Validator, mail: Mail):
        """ register a new customer and also checks that form is filled out properly without errors and checks to see if email, passwords, and
        usernames alread exits"""

        email = User.lists('email')
        user_name = User.lists('username')
        pws = User.lists('password')

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

        #Will display what errors where committed when filling out registration form.
        if errors:
            return request.back().with_errors(errors).with_input()

        #check to see if emails or usernames already exist
        accounts = [email, user_name]
        inputs = [request.input('email'), request.input('username')]
       
        for input in inputs:
            for account in accounts:
                if inputs[0] in accounts[0] and inputs[1] in accounts[1]:
                    return request.back().with_errors({'error': ['{} and {} already exists'.format(inputs[0], inputs[1])]})
                elif input in account:
                    return request.back().with_errors({'error': ['{} already exists'.format(input)]})

        # checking to see if password already exists
        for pw in pws:
            if bcrypt.checkpw(bytes(request.input('password'), 'utf-8'), bytes(pw, 'utf-8')):
                return request.back().with_errors({'error': ['Password already exists.  Please create a new password.']})

        if request.input('password') != request.input('password_confirm'):
            return request.back().with_errors({'error': ['Passwords do not match.  Please make sure passwords match']})


        #This registers a new account
        user = auth.register({
            'firstname': request.input('firstname'),
            'lastname': request.input('lastname'),
            'address': request.input('address'),
            'cell_phone': request.input('cell_phone'),
            'email':request.input('email'),
            'username': request.input('username'),
            'password': request.input('password')
        })
        #Checking to see if all inputs on registration form are in correct format.
        
        #Will send an email confirming account has been created.
        mail.send_from('jrquiles18@gmail.com').subject('Account Confirmation').to(request.input('email')).template('mail/mail').send()

        # Login the user
        if auth.login(request.input('email'), request.input('password')):
            # Redirect to the homepage
            return request.redirect('/')
        
        return request.back().with_input()

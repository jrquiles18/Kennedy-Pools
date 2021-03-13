"""A AccountUpdateController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.auth import Auth
from app.User import User
from masonite.validation import Validator




class AccountUpdateController(Controller):
    """AccountUpdateController Controller Class."""

    def __init__(self, request: Request):
        """AccountUpdateController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, request: Request):
        user = request.user()
        firstname = user.firstname
        lastname = user.lastname
        address = user.address
        cell = user.cell_phone
        email = user.email
        username = user.username
        password = user.password
        return view.render('account_update', {'firstname': firstname, 'lastname':lastname,
            'address': address, 'cell_phone': cell, 'email': email, 'username': username })

    def update(self, request: Request, validate: Validator, auth: Auth, view: View):
        user = User.all()
        customer = request.user()

        email = User.lists('email')
        user_name = User.lists('username')

        #Checks to see if updated email or username already exists
        if request.input('email') != customer.email:
            if request.input('email') in email:
                return request.back().with_errors({'error': ['{} already exists'.format(request.input('email'))]})
        elif request.input('username') != customer.username:
            if request.input('username') in user_name:
                return request.back().with_errors({'error': ['{} already exists'.format(request.input('username'))]})

        #Inputs to update customer information
        user.where('id', customer.id).first().update(firstname=request.input('firstname'))
        user.where('id', customer.id).first().update(lastname=request.input('lastname'))
        user.where('id', customer.id).first().update(address=request.input('address'))
        user.where('id', customer.id).first().update(cell_phone=request.input('cell_phone'))
        user.where('id', customer.id).first().update(email=request.input('email'))
        user.where('id', customer.id).first().update(username=request.input('username'))

        #Checks that all information is filled out properly
        errors = request.validate(validate.required(['firstname', 'lastname', 'address', 'email', 'username']),
                                    validate.email('email'))

        if errors:
            return request.back().with_errors(errors).with_input()
        else:
            request.session.flash('success', 'Your account has been successfully updated.')
            return request.redirect('account')

    

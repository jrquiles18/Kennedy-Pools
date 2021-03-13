"""A AccountCancelController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.validation import Validator
from masonite.validation import MessageBag
from masonite.auth import Auth
from masonite import Mail
from app.User import User
from app.CancelledAccount import CancelledAccount


import bcrypt

class AccountCancelController(Controller):
    """AccountCancelController Controller Class."""

    def __init__(self, request: Request):
        """AccountCancelController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View):
        return view.render('account_cancel')

    def cancel(sef, request: Request, auth: Auth, validate: Validator, mail: Mail ):
        user = User.all()
        customer = request.user()

        pw = customer.password

        reason = request.input('radio')
        confirm_password = request.input('password')

        #checking that all required fields are entered and no errors are found.
        errors = request.validate(
            validate.required(['radio', 'password'], messages = {'radio': "Please choose a reason for cancelling."}))

        if errors:
            return request.back().with_errors(errors)
        elif not bcrypt.checkpw(bytes(confirm_password, 'utf-8'), bytes(pw, 'utf-8')):
            return request.back().with_errors({'error': ["Are you sure that's the right password?"]})

        user_id = user.where('id', customer.id).first()
        # User.where('id', customer.id).where_null('cancelled').update(cancelled='Yes')
        User.where('id', customer.id).update(cancelled="Yes")
    
        CancelledAccount.insert({
            'user_id': user_id.id,
            'cancel_reason': request.input('radio'),
            'suggestions': request.input('suggestion')
        })

        request.session.flash('success', 'Your account has been successfully cancelled. Thank you for your business.')
        # mail.send_from('jrquiles18@gmail.com').subject('Cancellation Confirmation').to(customer.email).template('cancel', {'title': 'Kennedy Pools & Supplies'}).send()
        auth.logout()
        return request.redirect('/')

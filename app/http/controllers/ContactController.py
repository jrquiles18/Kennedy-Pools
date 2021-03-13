"""A ContactController Module."""

from masonite.request import Request
from masonite.auth import Auth
from masonite.view import View
from masonite.validation import Validator
from masonite.controllers import Controller
from masonite.validation import MessageBag
from masonite import Mail
from masonite.validation.decorators import validate
from masonite.validation import required


class ContactController(Controller):
    """ContactController Controller Class."""

    def __init__(self, request: Request):
        """ContactController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, request: Request):
        if not request.user():
            return request.redirect('/login')
        return view.render('contact.html')

    # @validate(required(['contact', 'subject']), back=True)
    def contact(self, request: Request, auth: Auth, validate: Validator, mail: Mail):
        user_email = request.user().email
        message = request.input('contact')
        message_subject = request.input('subject')

        errors = request.validate(
            validate.required(['subject', 'contact']),
        )
        if errors:
            return request.back().with_errors(errors)
        else:
            mail.send_from(user_email).subject(message_subject).to('jrquiles18@gmail.com').send(message)
            request.session.flash('success', 'Your message has been successfully sent!')

        return request.redirect('/')

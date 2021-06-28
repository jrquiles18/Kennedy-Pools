from masonite.api.resources import Resource
from app.User import User
from masonite.auth import Auth
from masonite.request import Request
from masonite.view import View

from masonite.api.serializers import JSONSerializer
# from masonite.api.authentication import JWTAuthentication

class UserResource(Resource, JSONSerializer):
    model = User
    methods = ['create', 'index', 'show', 'update', 'delete']

    def show(self, request: Request, view: View):
        user = self.model.find(request.param('id'))
        firstname = user.firstname
        lastname = user.lastname
        address = user.address
        cell_phone = user.cell_phone
        email = user.email
        username = user.username

        
        # return view.render('reregister', {'firstname': firstname, 'lastname': lastname, 'address': address, 'cell_phone': cell_phone,
        #                                 'email': email, 'username': username})
        return {'firstname': firstname, 'lastname': lastname, 'address': address, 'cell_phone': cell_phone,
                                        'email': email, 'username': username} 
    
    def index(self, request: Request, view: View):
        boolean = True
        clicked = True
        return [boolean, clicked]
"""A ScheduleController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.auth import Auth
from masonite.validation import Validator

from app.Schedule import Schedule
from app.User import User

class ScheduleController(Controller):
    """ScheduleController Controller Class."""

    def __init__(self, request: Request):
        """ScheduleController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, request: Request):
        user=request.user()

        # if not user:
        #     return request.redirect('/login')
        # else:
            # user=request.user()
        firstname = user.firstname
        lastname = user.lastname
        address = user.address
            
        return view.render('schedule', {"address": address, "firstname": firstname, "lastname": lastname})

    def schedule(self, request: Request, validate: Validator):
        user = User.all()
        customer = request.user()

        name = request.input('name')
        address = request.input('address')

         #checking that all required fields are entered and no errors are found.
        errors = request.validate(
            validate.required(['service_type','name', 'address', 'service_month', 
                                'service_day', 'service_time', 'day_time']))

        if errors:
            return request.back().with_errors(errors)

        schedule_id = user.where('id', customer.id).first()

        Schedule.insert({
            'schedule_id': schedule_id.id,
            'service': request.input('service_type'),
            'month': request.input('service_month'),
            'day': request.input('service_day'),
            'time': request.input('service_time'),
            'daytime': request.input('day_time')
        })

        am_times = ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00', '11:30', '12:00']
        pm_times = ['12:00', '12:30', '1:00', '1:30', '2:00', '2:30', '3:00', '3:30', '4:00', '4:30', '6:00', '6:30']

        if request.input('service_time') in pm_times and request.input('day_time') == 'AM':
            request.session.flash('success', "No morning appointments available for this time.")
            return request.back()
        
        elif request.input('service_time') in am_times and request.input('day_time') == 'PM':
            request.session.flash('success', "No evening appointments available for this time.")

        else:
            request.session.flash('success', 'Your appointment has been successfully scheduled!')
        
        return request.redirect('/')
    
        

        

        

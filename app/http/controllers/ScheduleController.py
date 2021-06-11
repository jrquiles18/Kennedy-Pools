"""A ScheduleController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from masonite.auth import Auth
from masonite.validation import Validator
from masonite import Mail

from app.Schedule import Schedule
from app.User import User
from app.Schedule import Schedule
from datetime import datetime

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
        firstname = user.firstname
        lastname = user.lastname
        address = user.address
        service_id = request.param('slug')

        return view.render('schedule', {"address": address, "firstname": firstname, "lastname": lastname, "service_id": service_id}) 

    def schedule(self, view: View, request: Request, validate: Validator, mail: Mail):
        user = User.all()
        customer = request.user()
        
        name = request.input('name')
        address = request.input('address')
        
        schedule_date_info =  request.input('date')
        path = request.path
    
         #checking that all required fields are entered and no errors are found.
        errors = request.validate(
            validate.required(['service_type', 'name', 'address']))
            
        if errors:
            return request.back().with_errors(errors)

        if not schedule_date_info[0] or not schedule_date_info[1]:
            request.session.flash('success', "The service date and service time is required.")
            return request.back()

        schedule_id = user.where('id', customer.id).first()
        
        Schedule.insert({
            'schedule_id': schedule_id.id,
            'service': request.input('service_type'),
            'service_date': schedule_date_info[0],
            'service_time': schedule_date_info[1], 
            'customer_name': request.input('name')
        })

        #getting the schedules table data
        customer_schedule = Schedule.get().last()
        
         #sends email with pool appointment schedule details
        mail.subject('Pool Appointment Confirmation').to(customer.email).template('appt_confirm', {'service': customer_schedule.service, 
                                'service_date':customer_schedule.service_date, 'service_time':customer_schedule.service_time}).send()
        
        request.session.flash('success', 'Your appointment has been successfully scheduled!  A confirmation email has been sent.')
        
        return request.redirect('/') 

    def update(self, view: View, request: Request, validate: Validator, mail: Mail):
        schedule_date_info =  request.input('date')
        customer = request.user()

        #checking that all required fields are entered and no errors are found.
        errors = request.validate(
            validate.required(['service_type', 'name', 'address']))
            
        if errors:
            return request.back().with_errors(errors)

        if not schedule_date_info[0] or not schedule_date_info[1]:
            request.session.flash('success', "The service date and service time is required.")
            return request.back()

        update_schedule = Schedule.where('id', '=', request.param('slug')).update(service=request.input('service_type'), 
            service_date=schedule_date_info[0], service_time=schedule_date_info[1])

        #need to changed this variable to current new updated info to send in email confirmation.
        customer_schedule = Schedule.get().last()

        #sends email with pool appointment schedule details
        # mail.subject('Pool Appointment Update Confirmation').to(customer.email).template('appt_confirm', {'service': customer_schedule.service, 
        #                         'service_date':customer_schedule.service_date, 'service_time':customer_schedule.service_time}).send()
        request.session.flash('success', 'Your appointment has been updated!  A confirmation email has been sent.')

        return request.redirect('/')
        
        

        

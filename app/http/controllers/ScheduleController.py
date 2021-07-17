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
from app.OneTimeService import OneTimeService
from datetime import datetime

import jwt

class ScheduleController(Controller):
    """ScheduleController Controller Class."""

    def __init__(self, request: Request):
        """ScheduleController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request

    def show(self, view: View, request: Request):
        token = request.param('token')
        # guest = OneTimeService.where('remember_token', token).get()
        # name = guest.pluck('customer_name')[0]
        # address = guest.pluck('address')[0]
        # email = guest.pluck('email')[0]
        # cell_phone = guest.pluck('cell_phone')[0]
        # service_id = guest.pluck('id')[0]
        if request.user():
            user=request.user()
            firstname = user.firstname
            lastname = user.lastname
            address = user.address
            service_id = request.param('slug')
            token = user.remember_token
            return view.render('schedule', {"address": address, "firstname": firstname, "lastname": lastname, "service_id": service_id, 'token': token}) 
        
        elif not request.user() and not token:
            # token = request.param('token')
            # return view.render('schedule', {'token': token})
            return view.render('schedule')

            # return view.render('schedule', {'name':name, 'address':address, 'email': email, 'cell_phone':cell_phone, 'token': token})
        elif not request.user():
            token = request.param('token')
            guest = OneTimeService.where('remember_token', token).get()
            name = guest.pluck('customer_name')[0]
            address = guest.pluck('address')[0]
            email = guest.pluck('email')[0]
            cell_phone = guest.pluck('cell_phone')[0]
            return view.render('schedule', {'name':name, 'address':address, 'email': email, 'cell_phone':cell_phone, 'token': token})

        else:
            return request.redirect('/login')

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
        mail.subject('Pool Appointment Confirmation').to(customer.email).template('mail/appt_confirm', {'service_id': customer_schedule.id, 'service': customer_schedule.service, 
                                'service_date':customer_schedule.service_date, 'service_time':customer_schedule.service_time}).send()
        
        request.session.flash('success', 'Your appointment has been successfully scheduled!  A confirmation email has been sent.')
        
        return request.redirect('/') 

    def cancel(self, request: Request):
        return 'hello'

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
        mail.subject('Pool Appointment Update Confirmation').to(customer.email).template('mail/appt_confirm', {'service_id': request.param('slug'), 'service': customer_schedule.service, 
                                'service_date':customer_schedule.service_date, 'service_time':customer_schedule.service_time}).send()
        request.session.flash('success', 'Your appointment has been updated!  A confirmation email has been sent.')

        return request.redirect('/')

    def reschedule(self, request: Request, validate: Validator, mail: Mail):
        errors = request.validate(
            validate.required(['service_type', 'name', 'address', 'email', 'cell_phone']))
        
        if errors:
            return request.back().with_errors(errors)
        
        token = request.param('token')
        decoded_token = jwt.decode(token, 'secret', algorithm='HS256')
        guest = OneTimeService.where('email', decoded_token['email']).update(service=request.input('service_type'), customer_name=request.input('name'),
                                                                            address=request.input('address'), service_date=request.input('date')[0],
                                                                            service_time=request.input('date')[1], email=request.input('email'), 
                                                                            cell_phone=request.input('cell_phone'))

        email = request.input('email')
        encoded_jwt = jwt.encode({'email': email, 'httpMethod': 'GET'}, 'secret', algorithm='HS256', ).decode('utf-8') 

        mail.subject('Pool Appointment Confirmation').to(request.input('email')).template('mail/appt_confirm_guest', {'service_id': request.param('slug'), 'service': request.input('service_type'),
            'service_date': request.input('date')[0], 'service_time': request.input('date')[1], 'token': encoded_jwt }).send()

        request.session.flash('success', 'Your appointment has been successfully rescheduled!  A confirmation email has been sent.')
        return request.redirect('/') 

    def once(self, request: Request, validate: Validator, mail: Mail):
        email = request.input('email')
        encoded_jwt = jwt.encode({'email': email, 'httpMethod': 'GET'}, 'secret', algorithm='HS256', ).decode('utf-8')

        errors = request.validate(
            validate.required(['service_type', 'name', 'address', 'email', 'cell_phone']))
            
        if errors:
            return request.back().with_errors(errors)

        OneTimeService.insert({
            'service': request.input('service_type'),
            'customer_name': request.input('name'),
            'address': request.input('address'),
            'service_date': request.input('date')[0],
            'service_time': request.input('date')[1],
            "email": request.input('email'),
            'cell_phone': request.input('cell_phone'),
            'remember_token': encoded_jwt
        })

        email = request.input('email')
        encoded_jwt = jwt.encode({'email': email, 'httpMethod': 'GET'}, 'secret', algorithm='HS256', ).decode('utf-8')

        mail.subject('Pool Appointment Confirmation').to(request.input('email')).template('mail/appt_confirm_guest', {'service': request.input('service_type'),
            'service_date': request.input('date')[0], 'service_time': request.input('date')[1], 'token': encoded_jwt }).send()
       
        request.session.flash('success', 'Your appointment has been successfully scheduled!  A confirmation email has been sent.')

        return request.redirect('/') 
        
        

        

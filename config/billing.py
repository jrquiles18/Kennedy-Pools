''' Masonite Billing Settings '''

import os

#the processor that Masonite billing will use
DRIVER = 'stripe'

#configuration setting for the driver
DRIVERS = {
    'stripe': {
        'client': os.getenv('STRIPE_CLIENT'),
        'secret': os.getenv('STRIPE_SECRET'),
        'currency': 'usd',
    }
}

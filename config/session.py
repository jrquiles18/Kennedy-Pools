"""Session Settings."""

from masonite import env

"""Session Driver
Sessions are able to be linked to an individual user and carry data from
request to request. The memory driver will store all the session data
inside memory which will delete when the server stops running.

Supported: 'memory', 'cookie'
"""

DRIVER = env('SESSION_DRIVER', 'cookie')

DRIVERS = {
    'cookie': {
        'flash_expires': '1 minute' # This is now setting the flash cookie time. Can set this to 1 hour if you want.
    }
}
"""User Model."""

from config.database import Model


class User(Model):
    """User Model."""

    __fillable__ = ['firstname', 'lastname', 'address', 'email', 'username', 'password', 'cell_phone', 'cancelled']

    __auth__ = 'email'

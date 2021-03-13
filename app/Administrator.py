"""Administrator Model."""

from config.database import Model


class Administrator(Model):
    """Administrator Model."""

    __fillable__ = ['admin_name', 'admin_cell_phone', 'admin_address', 'admin_email', 'admin_username', 'password']

    __auth__ = 'email'

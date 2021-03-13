"""Technician Model."""

from config.database import Model


class Technician(Model):
    """Technician Model."""
    __fillable__ = ['pool_tech_name', 'pool_tech_cell_phone', 'pool_tech_address', 'pool_tech_email', 'pool_tech_username', 'password']

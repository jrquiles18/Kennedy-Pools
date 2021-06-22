"""OneTimeService Model."""

from config.database import Model


class OneTimeService(Model):
    """OneTimeService Model."""
    __fillable__ = ['service', 'service_date', 'service_time', 'customer_name', 'address','email', 'cell_phone','service_state', 'cancelled_on']
   
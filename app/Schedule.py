"""schedule Model."""

from config.database import Model
from orator.orm import belongs_to


class Schedule(Model):
    """schedule Model."""
    # __fillable__ = ['service', 'month', 'day', 'time', 'daytime', 'schedule_id']
    __fillable__ = ['service', 'service_date', 'service_time', 'schedule_id', 'customer_name', 'service_state', 'cancelled_on']
   
    
    @belongs_to('schedule_id', 'id')
    # def schedule(self):
    def customer(self):
        from app.User import User  #import here to avoid circular dependencies
        return User


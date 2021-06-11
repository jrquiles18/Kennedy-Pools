"""User Model."""

from config.database import Model
from orator.orm import belongs_to


class User(Model):
    """User Model."""

    __fillable__ = ['firstname', 'lastname', 'address', 'email', 'username', 'password', 'cell_phone', 'cancelled']

    __auth__ = 'email'

    @belongs_to('id', 'schedule_id')
    def schedule(self):
        from app.Schedule import Schedule  #import here to avoid circular dependencies
        return Schedule


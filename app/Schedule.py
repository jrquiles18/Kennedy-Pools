"""schedule Model."""

from config.database import Model
from orator.orm import belongs_to


class Schedule(Model):
    """schedule Model."""
    __fillable__ = ['service', 'month', 'day', 'time', 'daytime', 'schedule_id']


    @belongs_to('schedule_id', 'id')
    def schedule(self):
        from app.User import User  #import here to avoid circular dependencies
        return User


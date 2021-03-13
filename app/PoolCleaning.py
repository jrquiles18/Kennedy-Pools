"""PoolCleaning Model."""

from config.database import Model


class PoolCleaning(Model):
    """PoolCleaning Model."""
    __fillable__ = ['service_id', 'pool_technician', 'service_performed', 'service_date']

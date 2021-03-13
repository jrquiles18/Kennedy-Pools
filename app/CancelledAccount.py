"""CancelledAccount Model."""

from config.database import Model


class CancelledAccount(Model):
    """CancelledAccount Model."""
    __fillable__ = ['user_id', 'cancel_date', 'cancel_reason', 'suggestions']

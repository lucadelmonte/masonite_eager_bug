""" User Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_one

class User(Model):
    """User Model"""

    __table__ = 'user'

    __appends__ = ['address']

    @has_one('user_id', 'id')
    def address(self):
        from .Address import Address
        return Address

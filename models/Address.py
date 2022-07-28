""" Address Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to

class Address(Model):
    """Address Model"""

    __table__ = 'address'

    @belongs_to
    def user(self):
        from .User import User
        return User

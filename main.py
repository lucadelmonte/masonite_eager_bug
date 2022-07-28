from models.Address import Address
from models.User import User


for i in range(10):
    User.create()


import logging, sys

logger = logging.getLogger('masoniteorm.connection.queries')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

if len(sys.argv) > 1 and sys.argv[1] == 'eager':
    users = User.with_('address').all()
else:
    users = User.all()

users.serialize()

logger.setLevel(logging.INFO)

for user in users:
    user.delete()

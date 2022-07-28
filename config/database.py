import os
from masoniteorm.connections import ConnectionResolver

DATABASES = {
    'default': 'testing',
    'testing': {
        'driver': 'sqlite',
        'database': '/tmp/website-service',
        'log_queries': True
    },
}

DB = ConnectionResolver().set_connection_details(DATABASES)

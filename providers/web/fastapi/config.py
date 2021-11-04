import os

truthy_envvar_values = ['true', '1', 'yeesh']

APP_HOST = os.environ.get('APP_HOST', '0.0.0.0')
APP_PORT = int(os.environ.get('APP_PORT', '80'))

IS_DEBUG = 'IS_DEBUG' in os.environ and os.environ['IS_DEBUG'].lower() in truthy_envvar_values

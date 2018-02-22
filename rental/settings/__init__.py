import os

if os.environ.get('ENVIRONMENT')=='production':
    from .production import *
else:
    from .local import *

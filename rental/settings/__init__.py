import os

from .base import *

if os.environ.get("ENVIRONMENT") == "production":
    from .production import *
else:
    from .local import *

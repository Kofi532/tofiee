

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'realestate.settings')

# application = get_wsgi_application()

# +++++++++++ DJANGO +++++++++++
import os
import sys
path = '/home/kofi532/tofiee'
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'realestate.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
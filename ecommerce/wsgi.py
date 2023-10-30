"""
WSGI config for ecommerce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
<<<<<<< HEAD
settings_module = 'ecommerce.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'ecommerce.settings'
=======
settings_modul = 'azure_project.deployment' if 'WEBSITE_HOSTNAME' in os.environ else 'ecommerce.settings'
>>>>>>> 821e9686aad0c587ba8d27b27e7814b06cc70300

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

application = get_wsgi_application()

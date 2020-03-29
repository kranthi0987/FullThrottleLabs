"""
ASGI config for FullThrottleLabs project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

#  Copyright (c) 2020.  This repo or code maintained  by Sanjay kranthi
#  you can contact on this mail: kranthi0987@gmail.com
#  you can clone my projects git: github.com/kranthi0987

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FullThrottleLabs.settings')

application = get_asgi_application()

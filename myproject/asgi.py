"""
<<<<<<< HEAD
ASGI config for myproject project.
=======
ASGI config for myproject2 project.
>>>>>>> 20491f934666bd79a5b8c5dc2f756942736540cc

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
=======
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject2.settings')
>>>>>>> 20491f934666bd79a5b8c5dc2f756942736540cc

application = get_asgi_application()

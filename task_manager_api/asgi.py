"""
ASGI config for task_manager_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from tasks import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager_api.settings')

application = get_asgi_application()
# taskmanager/asgi.py

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager_api.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/tasks/", consumers.TaskConsumer.as_asgi()),
        ])
    ),
})

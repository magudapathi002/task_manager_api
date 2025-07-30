# tasks/urls.py

from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, user_info

# Swagger config
schema_view = get_schema_view(
    openapi.Info(
        title="Task Manager API",
        default_version='v1',
        description="Task management API with real-time updates, role-based access, and token auth.",
        contact=openapi.Contact(email="you@example.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# Router config
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
                  # path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
                  path('user-info/', user_info, name='user-info'),
              ] + router.urls

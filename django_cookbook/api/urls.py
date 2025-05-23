"""API URL configuration."""

from django.urls import include, path
from rest_framework import routers

from .views import GroupViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]

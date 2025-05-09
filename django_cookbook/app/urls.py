"""URL configuration."""

from django.urls import path

from .views import api_get, api_post_put, index, use_cache

urlpatterns = [
    path('', index, name='index'),
    path('api/get/', api_get, name='api_get'),
    path('api/post/', api_post_put, name='api_post_put'),
    path('use_cache/', use_cache, name='use_cache'),
]

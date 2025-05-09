"""API Permissions."""

from typing import Any, override

from django.http import HttpRequest
from rest_framework.permissions import BasePermission


class IsAdminUser(BasePermission):
    """
    Allows access only to superuser users.
    """

    @override
    def has_permission(self, request: HttpRequest, view: Any) -> bool:
        return bool(request.user and request.user.is_staff)  # type: ignore

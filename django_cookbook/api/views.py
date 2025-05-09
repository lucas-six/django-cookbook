"""API Views."""

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from rest_framework import viewsets

from .serializers import GroupSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.DjangoModelPermissions]
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('is_active',)
    search_fields = ('=id', 'username')
    ordering_fields = ('username', 'code', 'date_joined')  # '__all__'
    ordering = ('-date_joined', '-is_active', 'username')


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    search_fields = ('=id', 'name')
    ordering = ('name',)

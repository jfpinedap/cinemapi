"""Person views"""

# Django imports
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework import viewsets
from rest_framework import filters

# Serialize imports
from .serializer import PersonSerializer

# Model imports
from .models import Person
  

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class PersonViewSet(viewsets.ModelViewSet):
    """
    Safe methods are publicly available, no authentication is required.
    Unsafe methods are only available to authenticated users.
    Person documents includes references to movies in the different roles the Person has.
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['last_name']

    permission_classes = [IsAuthenticated|ReadOnly]

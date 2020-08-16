"""Movie views"""

# Django imports
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework import viewsets
from rest_framework import filters

# Serialize imports
from .serializer import MovieSerializer

# Model imports
from .models import Movie
  

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class MovieViewSet(viewsets.ModelViewSet):
    """
    Safe methods are publicly available, no authentication is required.
    Unsafe methods are only available to authenticated users.
    Movie documents includes full documents to persons in their different roles.
    Movie documents includes the Release Year in roman numerals. This field is not stored in the DB, just calculated on the fly.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['release_year', 'title']

    permission_classes = [IsAuthenticated|ReadOnly]

"""Cinemapi URL Configuration"""

# Django imports
from django.conf.urls import url
from django.conf import settings
from django.urls import include, path, re_path
from django.contrib import admin
from django.contrib.auth import views as auth_views

# rest framework imports
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# views imports
from cinemapi.persons.views import PersonViewSet
from cinemapi.movies.views import MovieViewSet


schema_view = get_schema_view(
   openapi.Info(
      title="Cinema API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'api/persons', PersonViewSet, basename='person')
router.register(r'api/movies', MovieViewSet, basename='movie')

urlpatterns = [
    path('admin/', admin.site.urls),    
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
    url(r'^redoc/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

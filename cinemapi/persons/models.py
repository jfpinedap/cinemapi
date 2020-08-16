"""Person model"""

# Django imports
from django.db import models

# Model imports
from cinemapi.movies.models import Movie


class Person(models.Model):
    """Person model."""
    last_name = models.CharField(max_length=225)
    first_name  = models.CharField(max_length=225)
    aliases = models.CharField(max_length=225)

    movies_as_actor = models.ManyToManyField(
        Movie, related_name='casting', blank=True
    )

    movies_as_director = models.ManyToManyField(
        Movie, related_name='directors', blank=True
    )

    movies_as_producer = models.ManyToManyField(
        Movie, related_name='producers', blank=True
    )
"Movie model"

# Base imports
import datetime

# Django imports
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


FIRST_MOVIE_DATE = 1878

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)

class Movie(models.Model):
    """Movie model."""
    title = models.CharField(max_length=225)
    overview = models.TextField()

    release_year = models.PositiveIntegerField(
        default=current_year(),
        validators=[
            MinValueValidator(FIRST_MOVIE_DATE),
            max_value_current_year
        ]
    )
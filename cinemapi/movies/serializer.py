"""Movie Serializer"""

# Django imports
from rest_framework import serializers
from cinemapi.persons.serializer import PersonSerializer

# Model imports
from .models import Movie

# Util imports
from .utils import int_to_roman


class MovieSerializer(serializers.ModelSerializer):
    casting = PersonSerializer(many=True, read_only=True)
    directors = PersonSerializer(many=True, read_only=True)
    producers = PersonSerializer(many=True, read_only=True)
    roman_release_year = serializers.SerializerMethodField('get_roman_year')

    def get_roman_year(self, movie):
        return int_to_roman(input_int=movie.release_year)

    class Meta:
        ordering = ['-id']
        model = Movie
        fields = (
            "id", "title", "overview",
            "release_year", "roman_release_year",
            "casting", "directors", "producers"
        )
        extra_kwargs = {
            'casting': {'required': False},
            'directors': {'required': False},
            'producers': {'required': False}
        }
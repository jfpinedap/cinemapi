"""Person Serializer"""

# Django imports
from rest_framework import serializers

# Model imports
from .models import Person

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        ordering = ['-id']
        model = Person
        fields = '__all__'
        extra_kwargs = {
            'movies_as_actor': {'required': False},
            'movies_as_director': {'required': False},
            'movies_as_producer': {'required': False}
        }

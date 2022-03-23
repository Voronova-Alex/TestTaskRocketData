from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id',
                  'last_name',
                  'first_name',
                  'middle_name',
                  'department',
                  'employment_date',
                  'salary_per_period',
                  'person_rating',
                  'manager')

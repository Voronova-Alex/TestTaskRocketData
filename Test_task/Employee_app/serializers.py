from rest_framework import serializers
from .models import Person
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "username", "first_name", "last_name", "password")



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



from .models import Person
from .serializers import PersonSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.mixins import LoginRequiredMixin

class APIPerson(LoginRequiredMixin, generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['person_rating']


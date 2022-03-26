from .models import Person
from .serializers import PersonSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authentication import TokenAuthentication, BasicAuthentication, SessionAuthentication


class APIPersons(LoginRequiredMixin, generics.ListAPIView):
    login_url = '/login/login'
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['person_rating']
    authentication_classes = (SessionAuthentication,)


class APIPerson(generics.ListAPIView):
    serializer_class = PersonSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return Person.objects.filter(first_name=user.first_name, last_name=user.last_name)

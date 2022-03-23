from django.urls import path
from .views import APIPerson

urlpatterns = [
    path('', APIPerson.as_view()),

    ]
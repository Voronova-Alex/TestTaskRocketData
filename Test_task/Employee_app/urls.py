from django.urls import path, re_path, include
from .views import APIPersons, APIPerson

urlpatterns = [
    path('', APIPersons.as_view()),
    path('login/', include('rest_framework.urls')),
    path('api', APIPerson.as_view()),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))

]

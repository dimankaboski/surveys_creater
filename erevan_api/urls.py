from django.urls import path
from django.conf.urls import url

from .views import *

app_name = 'api'

urlpatterns = [
    path('get_team_members', get_team_members, name='get_team_members'),
    path('get_header_description', get_header_description, name='get_header_description'),
    path('get_activities', get_activities, name='get_activities'),
    path('get_cases', get_cases, name='get_cases'),
]

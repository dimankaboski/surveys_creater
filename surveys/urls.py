from django.urls import path
from django.conf.urls import url

from .views import *

app_name = 'surveys'

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('create', CreateSurvey.as_view(), name='create_survey'),
    path('survey/<int:pk>', SurveyPublicOpened.as_view(), name='survey_public'),
    
]

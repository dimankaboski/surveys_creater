from django.urls import path
from django.conf.urls import url

from .views import *

app_name = 'surveys'

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('create', CreateSurvey.as_view(), name='create_survey'),
    path('survey/<int:pk>/statistic', SurveyStatistic.as_view(), name='survey_statistic'),
    path('survey/<int:pk>', SurveyPublicOpened.as_view(), name='survey_public'),
    path('survey/<uuid:uuid>', SurveyPassingByUrl.as_view(), name='survey_passing_by_url'),
    path('passed/<int:pk>', PassedSurveyDetail.as_view(), name='passed_survey'),
    path('complete', PassedSurveyComplete.as_view(), name='complete'),
]

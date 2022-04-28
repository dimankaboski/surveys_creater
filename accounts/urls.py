from django.urls import path
from django.conf.urls import url

from .views import *

app_name = 'auth'

urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('signup', Register.as_view(), name='signup'),
    path('logout', logout_view, name='logout'),
]

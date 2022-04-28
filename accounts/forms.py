from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'email']
    
    def __init__(self, *args, **kwargs):
       super(RegisterForm, self).__init__(*args, **kwargs)
       self.fields['first_name'].required = True
       self.fields['last_name'].required = True
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import custom_user_model

class RegistrationForm(UserCreationForm):
    class Meta:
        model= custom_user_model
        fields = ('username','password1','password2','email','contact_no','gender','address')
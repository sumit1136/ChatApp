from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    
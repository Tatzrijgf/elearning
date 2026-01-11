from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.contrib.auth.models import User

class Userform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'password1', 'password2']

class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'photo_profile', 'type_profile']        
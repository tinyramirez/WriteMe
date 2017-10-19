from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from WMUser.models import WMUser

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='required.')
    last_name = forms.CharField(max_length=30, required=True, help_text='required.')

    class Meta:
        model = WMUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', )
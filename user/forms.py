from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(label='Employee Id', widget=forms.TextInput(
            attrs={'autocomplete': 'off'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'required': True}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'required': True})) 

    class Meta:
        model = User       

        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = False

class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    
    username = forms.CharField(label='Employee Id', widget=forms.TextInput(
        attrs={'autocomplete': 'off', 'autofocus': True}))
    
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'autocomplete': 'off',
        }))
from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=50, required=True)
    last_name = forms.CharField(label='Last Name', max_length=50, required=True)
    email = forms.EmailField(label='Email', required=True)
    username = forms.CharField(label='Username', max_length=50, required=True)
    eth_address = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'eth_address', 'username', 'password', 'confirm_password')


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
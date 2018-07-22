from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', max_length=50, required=True)
    last_name = forms.CharField(label='Last Name', max_length=50, required=True)
    email = forms.EmailField(label='Email', required=True)
    username = forms.CharField(label='Username', max_length=50, required=True)
    eth_address = forms.CharField(max_length=43, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'eth_address', 'username', 'password', 'confirm_password')

    def clean_eth_address(self):
        eth_address = self.cleaned_data.get('eth_address')
        if eth_address:
            if len(eth_address) != 42:
                raise forms.ValidationError("Ethereum Address Must be of length 42.")
        else:
            raise forms.ValidationError("Enter the Ethereum Address")
        return eth_address


class BuyForm(forms.Form):
    item_id = forms.IntegerField(widget=forms.HiddenInput(), required=True)
    updated_price = forms.CharField(widget=forms.HiddenInput(), required=True)

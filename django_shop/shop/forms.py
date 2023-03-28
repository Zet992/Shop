from django import forms


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(label='Your email', max_length=100)
    password = forms.PasswordInput(label='Your password', max_length=100)

from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=35, label='Username')
    password = forms.CharField(min_length=6,
                               max_length=50,
                               label='Passwort',
                               widget=forms.PasswordInput)
    email = forms.EmailField(label='Email')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError('ame bereits vergeben')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('E-Mail-Adresse bereits registriert')
        return email

class LoginForm(forms.Form):
    username = forms.CharField(max_length=35, label='Username')
    password = forms.CharField(min_length=6,
                               max_length=50,
                               label='Passwort',
                               widget=forms.PasswordInput)
    
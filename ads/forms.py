from django import forms
from django.contrib.auth.models import User
from .models import Ad


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password_confirmed = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirmed = cleaned_data.get('password_confirmed')

        if password and password_confirmed and password != password_confirmed:
            raise forms.ValidationError('Пароли не совпадают.')

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Пользователь с таким именем уже существует.')

        return username


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description', 'price']

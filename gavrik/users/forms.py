from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import TextInput
from .models import CustomUser


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password = forms.CharField(label="",
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Логин'}))
    password1 = forms.CharField(label="",
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label="",
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Повтор пароля'}))

    email = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
    first_name = forms.CharField(label='',
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first_name'}))
    last_name = forms.CharField(label='',
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last_name'}))
    phone_number = forms.CharField(label='',
                                   widget=forms.TextInput(
                                       attrs={'class': 'form-control', 'placeholder': 'phone_number'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'phone_number']


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'avatar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

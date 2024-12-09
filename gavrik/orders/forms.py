from django.core.exceptions import ValidationError

from .models import Order
from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput


class CheckoutContactsForm(forms.Form):
    user_name = forms.CharField(required=True)
    user_phone = forms.CharField(required=True)

    def clean_user_name(self):
        pass

    def clean_user_phone(self):
        user_phone = self.cleaned_data.get('user_phone')
        if len(user_phone) != 12:  # Проверка, что телефон состоит только из цифр
            raise ValidationError('Неправильное количество символов в телефоне')
        return user_phone

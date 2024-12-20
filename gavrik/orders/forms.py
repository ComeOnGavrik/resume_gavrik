from django.core.exceptions import ValidationError

from .models import Order
from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput


class CheckoutContactsForm(forms.Form):
    user_name = forms.CharField(required=True)
    user_phone = forms.CharField(required=True)
    user_address = forms.CharField(required=True)
    user_comment = forms.CharField(required=False, widget=forms.Textarea)

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        return user_name

    def clean_user_phone(self):
        user_phone = self.cleaned_data.get('user_phone')
        if len(user_phone) != 13:
            raise ValidationError('Неправильное количество символов в телефоне!!!!!!!!!!!!!!!!!!!_')
        return user_phone

    def clean_user_comment(self):
        user_comment = self.cleaned_data.get('user_comment')
        return user_comment

    def clean_user_address(self):
        user_address = self.cleaned_data.get('user_address')
        return user_address


class OrderACallForm(forms.Form):
    subscriber_name = forms.CharField(required=True)
    subscriber_phone = forms.CharField(required=True)


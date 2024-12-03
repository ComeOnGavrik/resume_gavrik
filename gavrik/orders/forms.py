from .models import Order
from django import forms
from django.forms import ModelForm, TextInput, DateTimeInput


class CheckoutContactsForm(forms.Form):
    user_name = forms.CharField(required=True)
    user_phone = forms.CharField(required=True)


    # class Meta:
    #     model = Order
    #     fields = ['tittle', 'anons', 'full_text']
    #
    #     widgets = {
    #         "tittle": TextInput(attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Название статьи'
    #         }),
    #
    #         "anons": TextInput(attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Анонс статьи'
    #         }),
    #
    #         "full_text": TextInput(attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Полный текст'
    #         })
    #     }
from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['tittle', 'anons', 'full_text' ]

        widgets = {
            "tittle": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),

            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),

            "full_text": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Полный текст'
            })
        }
from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class Articles(models.Model):
    tittle = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=240)
    full_text = models.TextField('Статья')
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='articles', null=True,
                               default=None)

    def __str__(self):
        return self.tittle

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

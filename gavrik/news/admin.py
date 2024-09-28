from django.contrib import admin

# Register your models here.
from .models import Articles


#
class ArticlesAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)
    list_display = ['tittle', 'author', 'anons']
    search_fields = ['tittle']
    class Meta:
        model = Articles


admin.site.register(Articles, ArticlesAdmin)

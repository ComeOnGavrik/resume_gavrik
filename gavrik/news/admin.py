from django.contrib import admin

# Register your models here.
from .models import Articles
#
# admin.site.register(Articles)

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    readonly_fields = ('date',)

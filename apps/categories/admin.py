from django.contrib import admin
from apps.categories.models import Categories


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'description']

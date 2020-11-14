from django.contrib import admin
from apps.products.models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'image']
    list_display_links = ['pk']
    search_fields = ['name']
    list_filter = ['updated_at']
    readonly_fields = ['updated_at']

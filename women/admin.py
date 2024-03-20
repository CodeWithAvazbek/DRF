from django.contrib import admin
from .models import Category, Women


@admin.register(Women)
class WomenAmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'time_create', 'time_update', 'is_published', 'cat']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
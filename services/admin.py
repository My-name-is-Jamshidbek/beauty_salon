"""
admin page
"""
from django.contrib import admin
from .models import Category, Photo


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title',)


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('upload_date', )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Photo, PhotoAdmin)

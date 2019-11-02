from django.contrib import admin

# Register your models here.
from .models import Category, Photo

admin.site.register(Category)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "image", "uploded")

admin.site.register(Photo, PhotoAdmin)
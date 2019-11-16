from django.db import models
from django.db.models.signals import post_delete

import os

class Category(models.Model):
    name = models.CharField("Név", max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Kategóriák"

    def __str__(self):
        return self.name

class Photo(models.Model):

    name = models.CharField("Cím", max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="photos")
    description = models.TextField()
    uploded = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Fotók"

    def __str__(self):
        return self.name

def file_cleanup(sender, instance, **kwargs):
    os.remove(instance.image.path)

post_delete.connect(file_cleanup, sender=Photo)
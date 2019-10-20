from django.db import models

class Category(models.Model):
    name = models.CharField("Név", max_length=100)

    class Meta:
        verbose_name_plural = "Kategóriák"

    def __str__(self):
        return self.name
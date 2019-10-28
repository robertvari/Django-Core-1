from django.db import models

class Category(models.Model):
    name = models.CharField("Név", max_length=100)

    class Meta:
        verbose_name_plural = "Kategóriák"

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos')
    description = models.TextField()
    uploaded = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Photos"
    
    def __str__(self):
        return self.title
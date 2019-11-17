from django.db import models

# Create your models here.
class About(models.Model):
    name = models.CharField("Név", max_length=100)
    profile_pic = models.ImageField("Profilkép", upload_to="about")

    faceebook = models.URLField("Facebook URL", max_length=200, blank=True)
    instagram = models.URLField("Instagram URL", max_length=200, blank=True)
    phone = models.CharField("Telefon", max_length=200, blank=True)
    
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Magamról"
    
    def __str__(self):
        return self.name
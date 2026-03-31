from django.db import models

# Create your models here.
class Cuisine(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Cuisines'

    def __str__(self):
        ordering = ('name',)
        return self.name 
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Cuisine(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Cuisines'

    def __str__(self):
        ordering = ('name',)
        return self.name 

class Ingredient(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta: 
        def __str__(self):
            ordering = ('name',)
            return self.name 

class Meal(models.Model):
    meal_name = models.CharField(max_length=255)
    meal_description = models.TextField(blank= True)
    meal_cuisine_type = models.ForeignKey(Cuisine, on_delete= models.SET_NULL, null= True, blank =True)
    meal_ingredients= models.ManyToManyField(Ingredient, related_name="meals")
    meal_price = models.FloatField()
    meal_image = models.ImageField(upload_to='meal_images/', blank=True, null=True)
    meal_is_vegan = models.BooleanField(default=False)
    meal_is_vegetarian = models.BooleanField(default=False)
    meal_is_halal = models.BooleanField(default=False)
    meal_is_gluten_free = models.BooleanField(default=False)
    meal_is_nut_free = models.BooleanField(default=False)
    meal_created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="meals")
    meal_created_at = models.DateTimeField(auto_now_add=True)
    meal_location = models.CharField (max_length=8)



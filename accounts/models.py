from django.db import models
from food.models import Cuisine, Ingredient
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver


class User_Preference(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_cuisines = models.ManyToManyField(Cuisine,related_name= "preffered_cuisines",blank=True)
    disliked_cuisines = models.ManyToManyField(Cuisine,related_name= "disliked_cuisines", blank=True)
    preferred_ingredients = models.ManyToManyField(Ingredient, related_name= "preffered_ingredients", blank=True)
    disliked_ingredients = models.ManyToManyField(Ingredient, related_name= "disliked_ingredients", blank=True) 
    allergies = models.ManyToManyField(Ingredient, related_name="allergies", blank=True)
    is_vegan = models.BooleanField(default=False)
    is_vegetarian = models.BooleanField(default=False)
    is_halal = models.BooleanField(default=False)
    is_gluten_free = models.BooleanField(default=False)
    is_nut_free = models.BooleanField(default=False)
#having to use related name being a problem

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        User_Preference.objects.create(user=instance)
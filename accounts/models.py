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

    DIET_CHOICES = [
        ("None", "None"),
        ("Halal", "Halal"),
        ("Vegan", "Vegan"),
        ("Vegetarian", "Vegetarian"),
    ]
    
    dietary_requirements = models.CharField(max_length=20, choices=DIET_CHOICES, default="None")
    allergies = models.ManyToManyField(Ingredient, related_name="allergies", blank=True)

#having to use related name being a problem

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        User_Preference.objects.create(user=instance)
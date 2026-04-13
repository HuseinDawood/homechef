from django.contrib import admin

# Register your models here.
from . models import Cuisine, Meal, Ingredient
from accounts.models import User_Preference

admin.site.register(Cuisine)
admin.site.register(Meal)
admin.site.register(Ingredient)
admin.site.register(User_Preference)
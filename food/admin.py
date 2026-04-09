from django.contrib import admin

# Register your models here.
from . models import Cuisine, Meal, Ingredient

admin.site.register(Cuisine)
admin.site.register(Meal)
admin.site.register(Ingredient)
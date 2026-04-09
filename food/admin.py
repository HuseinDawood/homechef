from django.contrib import admin

# Register your models here.
from . models import Cuisine, Meal


admin.site.register(Cuisine)
admin.site.register(Meal)
from django.urls import path
from . import views

urlpatterns = [
    path("delete/<int:meal_id>/", views.delete_meal, name="delete_meal"),
]
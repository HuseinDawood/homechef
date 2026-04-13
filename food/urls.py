app_name = 'food'
from django.urls import path
from . import views

urlpatterns = [
    path("delete/<int:meal_id>/", views.delete_meal, name="delete_meal"),
    path("add/", views.add_meal, name="add_meal"),
    path('<int:pk>/edit/', views.edit_meal, name='edit'),
    path('discover/',views.browse_food, name="browse_food"),
    path('view/<int:meal_id>/', views.food_view, name='food_view'),
]
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Meal

@login_required
def delete_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id, meal_created_by=request.user)

    if request.method == "POST":
        meal.delete()
        return redirect("dashboard")

    if request.method == "POST":
        meal.delete()

    return redirect("dashboard")


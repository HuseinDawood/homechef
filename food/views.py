from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import MealForm
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

@login_required
def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES)

        if form.is_valid(): 
            meal = form.save(commit=False)
            meal.meal_created_by = request.user
            meal.save()
            form.save_m2m()

            return redirect('dashboard')
    else:
         form = MealForm()
     
    return render(request, 'food/form.html', {
        'form': form,

     })


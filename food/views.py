from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import MealForm, EditMealForm
from .models import Meal

@login_required
def delete_meal(request, meal_id):
    meal = get_object_or_404(Meal, id=meal_id, meal_created_by=request.user)

    if request.method == "POST":
        meal.delete()
        return redirect("accounts:dashboard")


    return redirect("accounts:dashboard")

@login_required
def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST, request.FILES)

        if form.is_valid(): 
            meal = form.save(commit=False)
            meal.meal_created_by = request.user
            meal.save()
            form.save_m2m()

            return redirect('accounts:dashboard')
    else:
         form = MealForm()
     
    return render(request, 'food/form.html', {
        'form': form,

     })

@login_required
def edit_meal(request, pk):
    meal = get_object_or_404(Meal, pk=pk, meal_created_by=request.user)
    if request.method == 'POST':
        form = EditMealForm(request.POST, request.FILES, instance=meal)

        if form.is_valid(): 
            form.save()

            return redirect('accounts:dashboard')
    else:
         form = EditMealForm(instance=meal)
     
    return render(request, 'food/form.html', {
        'form': form,
     })

def browse_food(request):
    listings= Meal.objects.all()
    return render (request, 'food/discover.html', {
        'listings': listings,
    })
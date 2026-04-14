from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import MealForm, EditMealForm
from .models import Meal
from accounts.models import User_Preference

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
        'is_edit': False,

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
        'is_edit': True,
     })

def browse_food(request):
    listings= Meal.objects.all()
    meal_scores = []
    for meal in listings:
        meal_score = calculate_match(request, meal.id)
        meal_scores.append((meal,meal_score))

    meal_scores.sort(key=lambda x: x[1], reverse=True)
    print(meal_scores)

    return render (request, 'food/discover.html', {
        'meal_scores': meal_scores,
    })

def food_view(request, meal_id):
    meal= get_object_or_404(Meal, id=meal_id)
    return render(request, 'food/food_view.html', {
        'meal': meal,
    })

def calculate_match(requested_user, meal_id):
    meal = get_object_or_404(Meal, id=meal_id)
    preference = get_object_or_404(User_Preference, user=requested_user.user)
    score = 0
    overall = 0 
    #if the cuisine matches
    if meal.meal_cuisine_type in preference.preferred_cuisines.all():
        score += 2
        overall += 2

    #if cuisine dont match
    if meal.meal_cuisine_type in preference.disliked_cuisines.all():
        score -= 2
        overall += 2   


    for ingredients in meal.meal_ingredients.all():
        overall +=1

        if ingredients in preference.preferred_ingredients.all():
            score +=1

        if ingredients in preference.disliked_ingredients.all():
            score -=1

        if ingredients in preference.allergies.all():
            return 0
        
    #treat these at instant red flags
    if preference.is_vegan and not meal.meal_is_vegan:
        return 0
    if preference.is_halal and not meal.meal_is_halal:
        return 0
    if preference.is_vegetarian and not meal.meal_is_vegetarian:
        return 0
    if preference.is_gluten_free and not meal.meal_is_gluten_free:
        return 0
    if preference.is_nut_free and not meal.meal_is_nut_free:
        return 0
    
    if overall > 0:
        print (score,overall)
        final_score= int((score/overall) * 100)
        if final_score > 0:
            return final_score
        else:
            return 0
    else:
        return 0


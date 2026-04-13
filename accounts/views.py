from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout 
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, EditPreferenceForm
from food.models import Meal
from .models import User_Preference



# Create your views here.
#hdawo@test.com husein



def dashboard(request):
    my_listings= Meal.objects.filter(meal_created_by=request.user)
    return render (request, 'accounts/dashboard.html', {
        'my_listings': my_listings,
    })

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid(): 
             form.save()
             return redirect('accounts:dashboard')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {
        'form': form

    })

def logout_user(request):
    logout(request)
    return redirect('core:index')

@login_required
def edit_preference(request):
    preference = get_object_or_404(User_Preference, user=request.user)
    if request.method == 'POST':
        form = EditPreferenceForm(request.POST, request.FILES, instance=preference)

        if form.is_valid(): 
            form.save()

            return redirect('accounts:dashboard')
    else:
         form = EditPreferenceForm(instance=preference)
     
    return render(request, 'accounts/preferences.html', {
        'form': form,
     })
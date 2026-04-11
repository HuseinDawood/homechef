from django.shortcuts import render, redirect

from .forms import SignupForm
from food.models import Meal



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
             return redirect('')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {
        'form': form

    })


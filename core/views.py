from django.shortcuts import render, redirect

from .forms import SignupForm
from django.http import HttpResponse



# Create your views here.
#hdawo@test.com husein

def index(request):
    return render(request, 'core/index.html')

def success(request):
    return HttpResponse("Logged in successfully")

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid(): 
             form.save()
             return redirect('')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form

    })

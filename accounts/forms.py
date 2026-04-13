from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import User_Preference

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Your Username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    email= forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder' : 'Your Email Address',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password1= forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Your Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Retype Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class LoginForm(AuthenticationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    password= forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder' : 'Your Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

class EditPreferenceForm(forms.ModelForm):
    class Meta:
        model = User_Preference
        fields = (
            'preferred_cuisines',
            'disliked_cuisines',
            'preferred_ingredients',
            'disliked_ingredients',
            'allergies',
            'is_vegan',
            'is_vegetarian',
            'is_halal',
            'is_gluten_free',
            'is_nut_free',
        )

        widgets = {
            'preferred_cuisines': forms.SelectMultiple(attrs={
                'class': INPUT_CLASSES
            }),
            'disliked_cuisines': forms.SelectMultiple(attrs={
                'class': INPUT_CLASSES
            }),
            'preferred_ingredients': forms.SelectMultiple(attrs={
                'class': INPUT_CLASSES
            }),
            'disliked_ingredients': forms.SelectMultiple(attrs={
                'class': INPUT_CLASSES
            }),
            'allergies': forms.SelectMultiple(attrs={
                'class': INPUT_CLASSES
            }),
        }
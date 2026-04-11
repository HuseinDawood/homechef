from django import forms
from .models import Meal

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = (
            'meal_name',
            'meal_description',
            'meal_cuisine_type',
            'meal_ingredients',
            'meal_price',
            'meal_image',
            'meal_is_vegan',
            'meal_is_vegetarian',
            'meal_is_halal',
            'meal_is_gluten_free',
            'meal_is_nut_free',
            'meal_location'
        )

        widgets = {
            'meal_name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'meal_description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'meal_cuisine_type': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'meal_ingredients': forms.SelectMultiple(attrs={
                'class': INPUT_CLASSES
            }),
            'meal_price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'meal_image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'meal_location': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
        }

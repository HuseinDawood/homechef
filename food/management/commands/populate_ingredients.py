from django.core.management.base import BaseCommand
from food.models import Ingredient


class Command(BaseCommand):
    help = "Populate the database with default ingredients"

    def handle(self, *args, **kwargs):
        ingredients = [
            # Proteins
            "Chicken",
            "Beef",
            "Lamb",
            "Turkey",
            "Salmon",
            "Tuna",
            "Prawns",
            "Eggs",
            "Tofu",
            "Halloumi",

            # Carbs
            "Rice",
            "Pasta",
            "Noodles",
            "Bread",
            "Potatoes",
            "Sweet Potato",
            "Tortilla",
            "Couscous",
            "Quinoa",

            # Vegetables
            "Onion",
            "Garlic",
            "Tomato",
            "Spinach",
            "Broccoli",
            "Carrot",
            "Mushrooms",
            "Bell Pepper",
            "Cucumber",
            "Lettuce",
            "Courgette",
            "Aubergine",
            "Peas",
            "Sweetcorn",

            # Dairy
            "Cheese",
            "Mozzarella",
            "Cheddar",
            "Parmesan",
            "Butter",
            "Milk",
            "Cream",
            "Yoghurt",

            # Herbs / spices
            "Salt",
            "Black Pepper",
            "Paprika",
            "Chilli Powder",
            "Cumin",
            "Turmeric",
            "Curry Powder",
            "Oregano",
            "Basil",
            "Parsley",
            "Coriander",

            # Sauces / extras
            "Olive Oil",
            "Soy Sauce",
            "Tomato Sauce",
            "Mayonnaise",
            "Ketchup",
            "Mustard",
            "Honey",
            "Lemon Juice",
            "Lime Juice",
            "Coconut Milk",

            # Common extras
            "Chickpeas",
            "Kidney Beans",
            "Lentils",
            "Avocado",
            "Flour",
            "Sugar",
        ]

        created_count = 0

        for ingredient_name in ingredients:
            obj, created = Ingredient.objects.get_or_create(name=ingredient_name)
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f"Added: {ingredient_name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Already exists: {ingredient_name}"))

        self.stdout.write(self.style.SUCCESS(
            f"\nDone! {created_count} new ingredients added."
        ))
from InCook import *
from account.models import *
from recipe.models import *
from django.shortcuts import render

def main (request):
    category = ["Dairy", "Meats", "Vegetables",
                "Fruits", "Spices", "Fish",
                "Baking and Grains", "Oils", "Seafood",
                "Nuts", "Desserts", "Beverages",
                "Soup", "Sauces", "Alcohol"]
    ingre_list = [[] for j in range(15)]
    ingre = Ingredient.objects.all()
    for i in ingre:
        if i.category in category:
            ingre_list[category.index(i.category)].append(i.name)

    return render(request, 'main.html', {})

from InCook import *
from account.models import *
from recipe.models import *
from django.shortcuts import render
import json

def main (request):
    category = ["Dairy", "Meats", "Vegetables",
                "Fruits", "Spices", "Fish",
                "Baking and Grains", "Oils", "Seafood",
                "Nuts", "Desserts", "Beverages",
                "Soup", "Sauces", "Alcohol"]
    ingre_list = [[] for j in range(15)]
    ingre = Ingredient.objects.all().order_by('-category')
    ingre_json = {}

    for i in ingre:
        if i.category in category:
            ingre_list[category.index(i.category)].append(i.name)

    cnt = 0
    for i in category:
        ingre_json[i] = ingre_list[cnt]
        cnt = cnt + 1

    return render(request, 'main.html', {'ingredient_list' : json.dumps(ingre_json)})

from django.db import models
from recipe.models import *
import json
ingre_list = ["beef", "butter", "chicken", "egg", "milk", "yogurt", "cheese", "bacon", "sausage", "ham", "pork", "turkey", "pepperoni", "salami", "lamb", "duck", "garlic", "onion", "olive", "tomato", "potato", "carrot", "basil", "rosemary", "pepper", "corn", "ginger", "mint", "mushroom", "broccoli", "lemon", "apple", "banana", "coconut", "mango", "lime", "orange", "pineapple", "strawberry", "blueberry", "grape", "peach", "pear", "cherry", "kiwi", "watermelon", "papaya", "tuna", "salmon"]
for ingre in ingre_list:
    with open("/django/InCook/static/InCookData/" + ingre + ".json") as data_file:
        data = json.load(data_file)
        for cook_elem in data['hits']:
            recipe = cook_elem['recipe']
            #recipe_url = recipe['url']
            author = "chunggilee"
            user = User.objects.get(username = author)
            direction = recipe['url']
            image = recipe['image']
            #totalWeight = recipe['totalWeight']
            name = recipe['label']
            ingredients = recipe['ingredients']
            #totalDaily = json.dumps(recipe['totalDaily'])
            dietLabels = recipe['dietLabels']
            calories = recipe['calories']
            healthLabels = recipe['healthLabels']
            #digest = json.dumps(recipe['digest'])
            cautions = recipe['cautions']
            thumbnail = name + ".jpg"
            print(type(dietLabels))
            #likeNum = 0
            #tools = None
            #category = None
            recipe = Recipe(direction = direction, url = image, name = name, diet_labels = dietLabels, calories = calories, health_labels = healthLabels, cautions = cautions, author = user, thumbnail = thumbnail)
            recipe.save()
            ingre_name_list = []
            ingre = Ingredient.objects.all()
            for i in ingre:
                ingre_name_list.append(i.name)
            for ing in ingredients:
                is_found = False
                for j in ingre_name_list:
                    if ing['text'].find(j) != -1:
                        if Ingredient.objects.filter(name=j).exists() and is_found == False:
                            is_found = True
                            ingredient = Ingredient.objects.filter(name=j)
                            recipe.ingredients.add(ingredient[0])

from django.db import models
from web.models import *
import json
ingre_list = ["beef", "butter", "chicken", "egg", "milk", "yogurt", "cheese", "bacon", "sausage", "ham", "pork", "turkey", "pepperoni", "salami", "lamb", "duck", "garlic", "onion", "olive", "tomato", "potato", "carrot", "basil", "rosemary", "pepper", "corn", "ginger", "mint", "mushroom", "broccoli", "lemon", "apple", "banana", "coconut", "mango", "lime", "orange", "pineapple", "strawberry", "blueberry", "grape", "peach", "pear", "cherry", "kiwi", "watermelon", "papaya", "tuna", "salmon"]
for ingre in ingre_list:
    with open("/django/InCook/static/InCookData/" + ingre + ".json") as data_file:
        data = json.load(data_file)
        for cook_elem in data['hits']:
            recipe = cook_elem['recipe']
            recipe_url = recipe['url']
            image = recipe['image']
            totalWeight = recipe['totalWeight']
            name = recipe['label']
            ingredients = json.dumps(recipe['ingredients'])
            totalDaily = json.dumps(recipe['totalDaily'])
            dietLabels = str(recipe['dietLabels'])
            calories = recipe['calories']
            healthLabels = str(recipe['healthLabels'])
            digest = json.dumps(recipe['digest'])
            cautions = str(recipe['cautions'])
            likeNum = 0
            tools = None
            category = None
            cook_data = cook(recipe_url = recipe_url, image = image, totalWeight = totalWeight, name = name, ingredients = ingredients, totalDaily = totalDaily, dietLabels = dietLabels, calories = calories, healthLabels = healthLabels, digest = digest, cautions = cautions, likeNum = likeNum, tools = tools, category = category)
            cook_data.save()
		

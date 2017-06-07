category = ["Dairy", "Meats", "Vegetables",
            "Fruits", "Spices", "Fish",
            "Baking and Grains", "Oils", "Seafood",
            "Nuts", "Desserts", "Beverages",
            "Soup", "Sauces", "Alcohol"]

ingre_list = [["butter", "egg", "milk", "parmesan", "cheddar", "cream", "cheese", "yogurt"],
         ["chicken", "beef", "bacon", "sausage", "ham", "steak", "pork", "turkey", "pepperoni", "salami", "chorizo", "ribs", "venison", "spam", "lamb", "duck"],
         ["garlic", "onion", "olive", "tomato", "potato", "salad", "carrot", "basil", "parsley", "rosemary", "pepper", "corn", "ginger", "mushroom", "broccoli", "spinach", "bean", "onion", "cucumber", "pickle", "potato", "mint"],
         ["lemon", "banana", "apple", "coconut", "mango", "lime", "orange", "pineapple", "berry", "berries", "grape", "peach", "pear", "cherry", "kiwi", "watermelon", "plum", "papaya", "apple"],
         ["powder", "flake", "seasoning", "herbs", "seed"],
         ["tuna", "salmon", "fish", "pollock", "carp"],
         ["germ", "flour", "rice", "pasta", "bread", "soda", "noodle", "bagel"],
         ["oil"],
         ["shrimp", "cockle", "crab", "lobster", "octopus", "squid"],
         ["nut", "almond"],
         ["chocolate", "craker", "marchmallow", "chips", "nutella"],
         ["juice", "coffe", "tea", "espresso", "coke", "sprite", "soda"],
         ["soup", "broth"],
         ["sauce", "paste", "gravy"],
         ["whisky", "beer", "wine", "rum", "brandy", "vodka", "gin"]]

from recipe.models import *
ingre = Ingredient.objects.all()
for i in ingre:
    for j in range(0, len(ingre_list)):
        for k in ingre_list[j]:
            if k in i.name:
                print(k)
                i.category = category[j]
                i.save()


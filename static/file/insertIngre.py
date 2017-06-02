with open('/django/InCook/ingredientlist.txt', 'r') as f:
   ingre_list = f.read()
   data = ingre_list.split("\n")
   for i in data:
       ingre = Ingredient(name = i)
       ingre.save()

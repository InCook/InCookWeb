from django.shortcuts import render

# Create your views here.

@login_required(login_url='/login', redirect_field_name='')
def recipe(request, recipe_id):
	if request.is_ajax():
		if Recipe.objects.filter(id=recipe_id).exists():
			recipe = Recipe.objects.get(id=recipe_id)
			account = Account.objects.get(id=request.user)

			name = recipe.name
			author = recipe.author
			thumbnail = recipe.thumbnail
			like_num = recipe.num_likes
			rating = recipe.score
			direction = recipe.direction

			bookmark = False
			if account.bookmarks.filter(id=recipe_id).exists():
				bookmark = True
			else:
				bookmark = False

			like = False
			if account.likes.filter(id=recipe_id).exists():
				like = True
			else:
				like = False
			
			ingredients = []
			for ing in recipe.ingredients.all():
				ingredients.append(ing.name)

			data = {'state':"Success", 'recipe_id':recipe_id, 'name':name, 'author':author, 'thumbnail':thumbnail, 'bookmark':bookmark, 'like':like, 'like_num':like_num, 'rating':rating, 'ingredients':ingredients, 'direction':direction}
			return HttpResponse(json.dumps(data), content_type="application/json")
	return HttpResponse(json.dumps({'state':"Fail"}), content_type="application/json")


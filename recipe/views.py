from django.shortcuts import render

# Create your views here.
@login_required(login_url='/login', redirect_field_name='')
def add(request):
	if request.is_ajax():
		form = RecipeForm()

		if request.method="POST":
			form = RecipeForm(request.POST)
			if form.is_valid():
				recipe = form.save()
				recipe.author = request.user
				recipe.created_date = timezone.now()
				recipe.name = request.POST.get('name')
				recipe.direction = request.POST.get('direction')
				recipe.thumbnaili = request.POST.get('thumbnail')
				recipe.url = request.POST.get('url')

				recipe.ingredients = request.POST.get('ingredients')

				recipe.health_labels = request.POST.get('health_labels')
				recipe.diet_labels = request.POST.get('diet_labels')
				recipe.cautions = request.POST.get('cautions')

				recipe.save()
				return HttpResponse('Success')
	return HttpResponse('Fail')
	
@login_requried(login_url='/login', redirect_field_name='')
def rating(request):
	if request.is_ajax():
		recipe_id = request.GET['recipe_id']
		new_rate = request.GET['rate']
		account = request.user
	
		# Check recipe id is int
		if recipe_id.isdigit() is not True:
			return HttpResponse('Fail');
		
		if Recipe.objects.filter(id=recipe_id).exists():
			recipe = Recipe.objects.get(id=recipe_id)

			# Already User give rating
			if Account.objects.filter(user__in=[account],ratings__in=[recipe]).exists():
				
			else:
				account.save()
				account.ratings.add(recipe)
				account.

		else:
			return HttpResponse('Fail')
	return HttpResponse('Fail')
	

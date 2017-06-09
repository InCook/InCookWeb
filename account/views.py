from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from recipe.models import *

# Create your views here.
@login_required(login_url='/login.html',redirect_field_name='')
def profile(request):
	if Account.objects.filter(user=request.user).exists():
		account = Account.objects.get(user=request.user)
	else:
		account = Account(user=request.user)
		account.save()

	received_like_recipe = Recipe.objects.filter(author = request.user)
	like_num = 0
	for i in received_like_recipe:
		like_num = like_num + i.no_likes

	recipes = Recipe.objects.all()
	booked_recipe = []
	for i in recipes:
		if Account.objects.filter(user__in=[request.user], bookmarks__in=[i]).exists():
			booked_recipe.append(i)

	ingre_dict = {}
	ingredients = Ingredient.objects.all()
	for ingre in ingredients:
		if ingre_dict.get(ingre.category):
			ingre_dict[ingre.category].append({ingre.id: ingre.name})
		else:
			ingre_dict[ingre.category] = [{ingre.id: ingre.name}]

	return render(request, 'profile.html',
					  {'title': 'InCook', 'recipes': booked_recipe, 'account': account, 'ingredients': ingre_dict, 'username': request.user, 'like_num':like_num})

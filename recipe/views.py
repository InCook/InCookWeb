import json
from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from operator import attrgetter
from functools import reduce
import operator

from .models import *
from .forms import RecipeForm
from account.models import *
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/login', redirect_field_name='')
def add_recipe(request):
	form = RecipeForm()

	if request.method == "POST":
		form = RecipeForm(request.POST)
		if form.is_valid():
			recipe = form.save(commit=False)
			recipe.author = request.user
			recipe.created_date = timezone.now()

			ingredients = str(request.POST.get('ing_names')).split(',')
			recipe.save()
			for ing in ingredients:
				if Ingredient.objects.filter(name=ing).exists():
					ingredient = Ingredient.objects.get(name=ing)
					recipe.ingredients.add(ingredient)
				else:
					new_ing = Ingredient(name=ing, category="")
					new_ing.save()
					recipe.ingredients.add(new_ing)

			recipe.health_labels = str(request.POST.get('hl')).split(',')
			recipe.diet_labels = str(request.POST.get('dl')).split(',')
			recipe.cautions = str(request.POST.get('c'))

			recipe.no_likes = 0
			recipe.score = 0.0

			recipe.save()
		
			return render(request, 'add.html', {})
		else:
			return HttpResponse("invalid") # invali d?????????????????????????
	return render(request,'add.html', {})
	
@login_required(login_url='/login', redirect_field_name='')
def add_rating(request):
	recipe_id = request.GET['recipe_id']
	new_rate = int(request.GET['rate'])

	# Check recipe id is int
	if recipe_id.isdigit() is not True:
		return HttpResponse("Fail");
	
	if Recipe.objects.filter(id=recipe_id).exists():
		recipe = Recipe.objects.get(id=recipe_id)

		# Already User give rating
		if Account.objects.filter(user = request.user, ratings = recipe).exists(): # pairrrrR?????????????
			account = Account.objects.get(user = request_user, ratings = recipe)
			account.save()
		else:
			account = Account(user = request.user)

		# avg rate => score? or calculation?
		rating = 1.0
		
		return HttpResponse(str(rating))
	return HttpResponse("Fail")
	
@login_required(login_url='/login', redirect_field_name='')
def get_recipe (request):
    recipe_id = request.GET['recipe_id']

    # Check recipe_id int
    if recipe_id.isdigit() is not True:
        response = json.dumps({'success': False, 'detail': "No matching type.", 'output': None})
        return HttpResponse(response, "application/json")

    # Check recipe existence
    if Recipe.objects.filter(id=recipe_id).exists():

        # Get attributes
        recipe = Recipe.objects.get(id=recipe_id)
        recipe_id = recipe.id
        name = recipe.name
        author = str(recipe.author)
        thumbnail = recipe.thumbnail
        ingre_list = recipe.ingredients.all()
        direction = recipe.direction

        ingredients = []
        for i in ingre_list:
            ingredients.append(str(i))

        # Check user existence
        if User.objects.filter(username=author).exists():
            user = User.objects.get(username=author)
        else:
            response = json.dumps({'success': False, 'detail': "No matching author.", 'output': None})
            return HttpResponse(response, "application/json")

        # Check Account existence
        if Account.objects.filter(user = user).exists():

            # bookmark or not
            if Account.objects.filter(user__in = [user], bookmarks__in = [recipe]).exists():
                bookmark = True
            else:
                bookmark = False

            # like or not
            if Account.objects.filter(user__in = [user], likes__in = [recipe]).exists():
                like = True
            else:
                like = False

        else:
            bookmark = False
            like = False

        # Count like_num and rating
        like_num = Account.objects.filter(likes = recipe).count()
        rating = Account.objects.filter(ratings = recipe).count()

        response = json.dumps({'success': True, 'detail': "Got recipe.", 'output': {"recipe_id" : recipe_id,
                             "name" : name, "author" : author, "thumbnail" : thumbnail, "bookmark" : bookmark,
                             "like" : like, "like_num" : like_num, "rating" : rating, "ingredients" : ingredients,
                             "direction" : direction}})
        return HttpResponse(response, "application/json")

    else:
        response = json.dumps({'success': False, 'detail': "No matching recipe.", 'output': None})
        return HttpResponse(response, "application/json")
    return HttpResponse(a, "application/json")

@login_required(login_url='/login', redirect_field_name='')
def add_like (request):
    recipe_id = request.GET['recipe_id']

    # Check recipe_id int
    if recipe_id.isdigit() is not True:
        response = json.dumps({'success': False, 'detail': "No matching type.", 'output': None})
        return HttpResponse(response, "application/json")

    like_str = ""
    like_num = 0
    like = False

    # Check recipe existence
    if Recipe.objects.filter(id=recipe_id).exists():

        # Get attributes
        recipe = Recipe.objects.get(id=recipe_id)
        author = str(recipe.author)

        # Check user existence
        if User.objects.filter(username=author).exists():
            user = User.objects.get(username=author)
        else:
            response = json.dumps({'success': False, 'detail': "No matching author.", 'output': None})
            return HttpResponse(response, "application/json")

        # Check Account existence
        if Account.objects.filter(user = user).exists():
            account = Account.objects.get(user = user)

            # Example
            # same thing but using in
            #users_in_1zone = User.objects.filter(zones__in=[ < id1 >])
            # filtering on a few zones, by id
            #users_in_zones = User.objects.filter(zones__in=[ < id1 >, < id2 >, < id3 >])

            # like or not
            if Account.objects.filter(user__in = [user], likes__in = [recipe]).exists():
                del_acc = Account.objects.filter(user__in = [user], likes__in = [recipe])
                del_acc[0].likes.remove(recipe)
                #del_acc.delete()
                like = False
            else:
                account.likes.add(recipe)
                like = True

            # Count like_num and rating
            like_num = account.likes.count()

            if like == True:
                like_str = "add_like-num"
            else :
                like_str = "delete_like-num"

        else:
            like = True
            account = Account(user = user)
            account.save()
            account.likes.add(recipe)
            like_str = "add_like-num"
            like_num = account.likes.count()

        response = json.dumps({'success': True, 'detail': "Got recipe.", 'output': {"recipe_id" : recipe_id,
                             "author" : author, like_str : like_num, "like" : like}})
        return HttpResponse(response, "application/json")

    else:
        response = json.dumps({'success': False, 'detail': "No matching recipe.", 'output': None})
        return HttpResponse(response, "application/json")
    return HttpResponse(a, "application/json")

@login_required(login_url='/login', redirect_field_name='')
def add_bookmark (request):
    recipe_id = request.GET['recipe_id']

    # Check recipe_id int
    if recipe_id.isdigit() is not True:
        response = json.dumps({'success': False, 'detail': "No matching type.", 'output': None})
        return HttpResponse(response, "application/json")

    like_str = ""
    like_num = 0
    like = False

    # Check recipe existence
    if Recipe.objects.filter(id=recipe_id).exists():

        # Get attributes
        recipe = Recipe.objects.get(id=recipe_id)
        author = str(recipe.author)

        # Check user existence
        if User.objects.filter(username=author).exists():
            user = User.objects.get(username=author)
        else:
            response = json.dumps({'success': False, 'detail': "No matching author.", 'output': None})
            return HttpResponse(response, "application/json")

        # Check Account existence
        if Account.objects.filter(user = user).exists():
            account = Account.objects.get(user = user)

            # Example
            # same thing but using in
            #users_in_1zone = User.objects.filter(zones__in=[ < id1 >])
            # filtering on a few zones, by id
            #users_in_zones = User.objects.filter(zones__in=[ < id1 >, < id2 >, < id3 >])

            # like or not
            if Account.objects.filter(user__in = [user], bookmarks__in = [recipe]).exists():
                del_acc = Account.objects.filter(user__in = [user], bookmarks__in = [recipe])
                del_acc[0].bookmarks.remove(recipe)
                bookmark = False
            else:
                account.bookmarks.add(recipe)
                bookmark = True

        else:
            bookmark = True
            account = Account(user = user)
            account.save()
            account.bookmarks.add(recipe)


        response = json.dumps({'success': True, 'detail': "Got recipe.", 'output': {"recipe_id" : recipe_id,
                             "bookmark" : bookmark}})
        return HttpResponse(response, "application/json")

    else:
        response = json.dumps({'success': False, 'detail': "No matching recipe.", 'output': None})
        return HttpResponse(response, "application/json")
    return HttpResponse(a, "application/json")
  
@login_required(login_url='/login', redirect_field_name='')
def search (request):
    # Get ingredients
    ingre_list = request.GET['ingredients']
    if ingre_list == "":
        response = json.dumps({'success': False, 'detail': "No matching ingredients.", 'output': None})
        return HttpResponse(response, "application/json")
    ingre_list = ingre_list.replace("\"", "")
    ingre_list = ingre_list.split(",")

    # Get username
    if request.GET['username'] != "":
        username = request.GET['username']
        username = username.replace("\"", "")
    else:
        username = None

    # Make query list in order to operate or opearation with respect to ingredients
    query_list = []
    for i in ingre_list:
        query_list.append(Q(name__contains = i))

    # Get all ingredients records
    ingredients = Ingredient.objects.filter(reduce(operator.or_, query_list))
    #ingredients = Ingredient.objects.filter(reduce(operator.and_, query_list))

    # Get recipe which contains ingredients
    rec = Recipe.objects.filter(ingredients = ingredients).distinct()

    output = []
    for i in rec:
        bookmark = False
        like = False

        # Check Account existence
        if username != "" and User.objects.filter(username=username).exists():
            user = User.objects.get(username)

            if Account.objects.filter(user=user).exists():

                # bookmark or not
                if Account.objects.filter(user__in=[user], bookmarks__in=[i]).exists():
                    bookmark = True
                else:
                    bookmark = False

                # like or not
                if Account.objects.filter(user__in=[user], likes__in=[i]).exists():
                    like = True
                else:
                    like = False
            else:
                bookmark = False
                like = False

        else:
            bookmark = False
            like = False

        # Count like_num and rating
        like_num = Account.objects.filter(likes=i).count()
        rating = Account.objects.filter(ratings=i).count()
        author = str(i.author)
        name = i.name
        thumbnail = i.thumbnail

        # Store output element
        output_elem = {}
        output_elem['author'] = author
        output_elem['name'] = name
        output_elem['thumbnail'] = thumbnail
        output_elem['like'] = like
        output_elem['bookmark'] = bookmark
        output_elem['like_num'] = like_num
        #output_elem['rating'] = rating

        ingre = []
        for j in i.ingredients.all():
            ingre_elem = {}
            ingre_elem['ingredient'] = j.name
            ingre.append(ingre_elem)

        output_elem['ingredients'] = ingre

        output.append(output_elem)

    response = json.dumps({'success': True, 'detail': "Got recipe.", 'output': output})
    return HttpResponse(response, "application/json")


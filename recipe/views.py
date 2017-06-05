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

def test(request):
    if Account.objects.filter(user=request.user).exists():
        account = Account.objects.get(user=request.user)
    else:
        account = Account(user = request.user)
        account.save()
    recipes = Recipe.objects.all()
    return render(request, 'base.html', {'title':'InCook', 'recipes': recipes, 'account':account})

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

            if not form.cleaned_data['hl']:
                recipe.health_labels = []
            else:
                recipe.health_labels = str(request.POST.get('hl')).split(',')
            if not form.cleaned_data['dl']:
                recipe.diet_labels = []
            else:
                recipe.diet_labels = str(request.POST.get('dl')).split(',')
            if not form.cleaned_data['c']:
                recipe.cautions = []
            else:
                recipe.cautions = str(request.POST.get('c'))

            recipe.no_likes = 0
            recipe.score = 0.0

            recipe.save()

            return render(request, 'add.html', {})
        else:
            return HttpResponse("invalid")
    return render(request,'add.html', {})

@login_required(login_url='/login', redirect_field_name='')
def add_rating(request):
    recipe_id = request.GET['recipe_id']
    new_rate = float(request.GET['rate'])

    # Check recipe id is int
    if recipe_id.isdigit() is not True:
        response = json.dumps({'success': False, 'detail': "No matching type.", 'output': None})
        return HttpResponse(response, "application/json")

    if Recipe.objects.filter(id=recipe_id).exists():
        recipe = Recipe.objects.get(id=recipe_id)
        if Account.objects.filter(user=request.user).exists():
            account = Account.objects.get(user=request.user)
            if Account.objects.filter(user__in=[request.user],ratings__in=[recipe]):
                account = Account.objects.get(user=request.user)
            else:
                account.ratings.add(recipe)
                account.save()
                recipe.score = recipe.score+new_rate
                recipe.participants = recipe.participants+1
                recipe.save()
            # avg rate
            if recipe.participants != 0:
                rating = recipe.score / recipe.participants
            else:
                rating = 0.0

            return HttpResponse(rating)
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
        if User.objects.filter(username=request.user).exists():
            user = User.objects.get(username=request.user)
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
        like_num = recipe.no_likes
        rating = recipe.score/recipe.participants

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

    if recipe_id.isdigit() is not True:
        response = json.dumps({'success': False, 'detail': "No matching type.", 'output': None})
        return HttpResponse(response, "application/json")

    if Recipe.objects.filter(id=recipe_id).exists():
        like = False
        recipe = Recipe.objects.get(id=recipe_id)
        if Account.objects.filter(user=request.user).exists():
            account = Account.objects.get(user=request.user)
            if Account.objects.filter(user__in=[request.user],likes__in=[recipe]).exists():
                recipe.no_likes = recipe.no_likes - 1
                recipe.save()
                account.likes.remove(recipe)
                account.save()
                like_num = recipe.no_likes
                like = False
            else:
                recipe.no_likes = recipe.no_likes + 1
                recipe.save()
                account.likes.add(recipe)
                account.save()
                like_num = recipe.no_likes
                like = True
        else:
            account = Account(user = request.user)
            account.save()
            recipe.no_likes = recipe.no_likes + 1
            recipe.save()
            account.likes.add(recipe)
            like_num = recipe.no_likes
            like = True

        response = json.dumps({'success': True, 'detail': "Added like.", 'output': {"recipe_id": recipe_id,
                                                                                    "like" : like,
                                                                                    "like_num" : like_num}})
        return HttpResponse(response, "application/json")

    else:
        response = json.dumps({'success': False, 'detail': "No matching recipe.", 'output': None})
        return HttpResponse(response, "application/json")

@login_required(login_url='/login', redirect_field_name='')
def add_bookmark (request):
    recipe_id = request.GET['recipe_id']
  
    if recipe_id.isdigit() is not True:
        response = json.dumps({'success': False, 'detail': "No matching type.", 'output': None})
        return HttpResponse(response, "application/json")

    if Recipe.objects.filter(id=recipe_id).exists():
        recipe = Recipe.objects.get(id=recipe_id)
        bookmark = False
        if Account.objects.filter(user=request.user).exists():
            account = Account.objects.get(user=request.user)
            if Account.objects.filter(user__in=[request.user],bookmarks__in=[recipe]).exists():
                account.bookmarks.remove(recipe)
                account.save()
                bookmark = False
            else:
                account.bookmarks.add(recipe)
                account.save()
                bookmark = True
        else:
            account = Account(user=request.user)
            account.bookmarks.add(recipe)
            account.save()
            bookmark = True
        response = json.dumps({'success': True, 'detail': "Added bookmark.", 'output': {"recipe_id": recipe_id,
                                                                                        "bookmark": bookmark}})
        return HttpResponse(response, "application/json")
    else:
        response = json.dumps({'success': False, 'detail': "No matching recipe.", 'output': None})
        return HttpResponse(response, "application/json")

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


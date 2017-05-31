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

from .models import *
from account.models import *
from django.contrib.auth.models import User

# Create your views here.

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
            account = Account.objects.get(user = user)

            # bookmark or not
            if account.bookmarks.count() == 0:
                bookmark = False
            else:
                bookmark = True

            # like or not
            if account.likes.count() == 0:
                like = False
            else:
                like = True

            # Count like_num and rating
            like_num = account.likes.count()
            rating = account.ratings.count()

        else:
            response = json.dumps({'success': False, 'detail': "No matching aacount.", 'output': None})
            return HttpResponse(response, "application/json")

        response = json.dumps({'success': True, 'detail': "Got recipe.", 'output': {"recipe_id" : recipe_id,
                             "name" : name,
                             "author" : author,
                             "thumbnail" : thumbnail,
                             "bookmark" : bookmark, "like" : like, "like_num" : like_num, "rating" : rating,
                             "ingredients" : ingredients,
                             "direction" : direction}})
        return HttpResponse(response, "application/json")

    else:
        response = json.dumps({'success': False, 'detail': "No matching recipe.", 'output': None})
        return HttpResponse(response, "application/json")
    return HttpResponse(a, "application/json")
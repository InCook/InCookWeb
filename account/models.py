from django.db import models
#from django_mysql.models import JSONField
from django.contrib.auth.models import User

from recipe.models import Recipe 

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(Recipe, related_name='account_ikes')
    bookmarks = models.ManyToManyField(Recipe, related_name='account_bookmarks')
    ratings = models.ManyToManyField(Recipe, related_name='account_ratings')
    #ratings_detail = JSONField() # { recipe_id : each score } -> MySQL 5.7+ is required

    def __str__(self):
        return self.user.first_name

from django.db import models
#from django_mysql.models import JSONField, ListCharField
from django_mysql.models import ListCharField
from django.contrib.auth.models import User
from django.utils import timezone

from .choices import *

class Ingredient(models.Model):
    category = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=50)
    direction = models.TextField()
    thumbnail = models.CharField(max_length=50, null=True)
    url = models.URLField(null=True, blank=True)
    ingredients = models.ManyToManyField(Ingredient)
    #ingredients_detail = JSONField() # { ingredients_id : amount } -> MySQL 5.7+ is required
    calories = models.FloatField(default=0, null=True, blank=True)
    health_labels = ListCharField(
        base_field=models.CharField(max_length=20), 
        size=15, max_length=15*21, 
        choices=HEALTH_LABELS, null=True, blank=True
    )
    diet_labels = ListCharField(
        base_field=models.CharField(max_length=20), 
        size=5, max_length=5*21,
        choices=DIET_LABELS, null=True, blank=True
    )
    cautions = ListCharField(
        base_field=models.CharField(max_length=20), 
        size=5, max_length=5*21,
        choices=DIET_LABELS, null=True, blank=True
    )
    no_likes = models.PositiveSmallIntegerField(default=0, null=True)
    score = models.FloatField(default=0, null=True) # total score
    participants = models.PositiveSmallIntegerField(default=0, null=True)

    def __str__(self):
        return self.name


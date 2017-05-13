from django.db import models
from django.utils import timezone
import json

# Create your models here.

class cook(models.Model):
	recipe_url = models.TextField(null=True)
	image = models.TextField(null=True)
	totalWeight = models.FloatField(null=True)
	name = models.CharField(max_length=255)
	ingredients = models.TextField(null=True)
	totalDaily = models.TextField(null=True)
	dietLabels = models.TextField(null=True)
	calories = models.FloatField(null=True)
	healthLabels = models.TextField(null=True)
	digest = models.TextField(null=True)
	caution = models.TextField(null=True)
	likeNum = models.IntegerField(blank=True, null=True)
	tools = models.TextField(null=True)
	category = models.CharField(max_length=255)
	



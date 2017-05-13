from django.db import models
from django.utils import timezone
import json

# Create your models here.

class cook(models.Model):
	recipe_url = models.TextField(null=True)
	image = models.TextField(null=True)
	totalWeight = models.FloatField(default = 0, null=True)
	name = models.CharField(max_length=255, null = True)
	ingredients = models.TextField(null=True)
	totalDaily = models.TextField(null=True)
	dietLabels = models.TextField(null=True)
	calories = models.FloatField(default = 0, null=True)
	healthLabels = models.TextField(null=True)
	digest = models.TextField(null=True)
	cautions = models.TextField(null=True)
	likeNum = models.IntegerField(default = 0, null=True)
	tools = models.TextField(null=True)
	category = models.CharField(max_length=255, null=True)
	



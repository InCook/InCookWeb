from django import forms
from django.contrib.auth.models import User
from django_mysql.models import ListCharField

from .models import Recipe

class RecipeForm(forms.ModelForm):
	ing_names = forms.CharField(max_length=200)
	hl = forms.CharField(max_length=200, required=False)
	dl = forms.CharField(max_length=200, required=False)
	c = forms.CharField(max_length=200, required=False)
	class Meta:
		model = Recipe
		fields = ('name','direction','thumbnail','url','ing_names','calories','hl','dl','c',)

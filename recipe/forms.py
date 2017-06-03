from django import forms
from django.contrib.auth.models import User

from .models import Recipe

class RecipeForm(forms.ModelForm):
	class Meta:
		model = Recipe
		fields = ('id', 'name','direction','thumbnail','ingredients','url','calories','health_labels','diet_labels','cautions',)

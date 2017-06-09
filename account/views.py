from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='/login.html',redirect_field_name='')
def profile(request):
	if Account.objects.filter(user=request.user).exists():
		account = Account.objects.get(user=request.user)
		name=request.user.username
		likes = []
		for recipe in account.likes.all():
			if Recipe.objects.filter(id=recipe.id).exists():
				likes.append(recipe.name)

		return render(request, 'profile.html',{'username':name,'likes':likes})
	return render(request,'profile.html',{})

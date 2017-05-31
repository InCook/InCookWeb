from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views as recipe_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'InCook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^recipe/$', recipe_views.get_recipe, name='get_recipe'),
]

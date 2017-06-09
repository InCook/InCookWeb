from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from recipe import views as recipe_views
from account import views as account_views
from . import views as incook_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'InCook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^$', incook_views.main,  name=''),
    url(r'^main$', recipe_views.test, name='main'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
	url(r'^profile$', account_views.profile, name='profile'),
    url(r'^recipe/$', recipe_views.get_recipe,  name='get_recipe'),
    url(r'^like/$', recipe_views.add_like,  name='add_like'),
    url(r'^bookmark/$', recipe_views.add_bookmark,  name='add_bookmark'),
    url(r'^add/$', recipe_views.add_recipe, name='add_recipe'),
    url(r'^rating/$', recipe_views.add_rating,  name='add_rating'),
    url(r'^search/$', recipe_views.search,  name='search'),
    url(r'^get-ingredients/$', recipe_views.get_ingredients,  name='get_ingredients'),
    url(r'^test/$', recipe_views.test,  name='test'),
]

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from recipe import views as recipe_views

urlpatterns = [
    # Examples:
    # url(r'^$', 'InCook.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^recipe/$', recipe_views.get_recipe,  name='get_recipe'),
    url(r'^like/$', recipe_views.add_like,  name='add_like'),
    url(r'^bookmark/$', recipe_views.add_bookmark,  name='add_bookmark'),
]

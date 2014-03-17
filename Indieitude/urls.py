from django.conf.urls import patterns, include, url
from home import views
from profiles import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'indieitude.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    
    #Base File for templates to extend
    url(r'^$', 'home.views.base', name="base"),
    
    #For User Registration
    url(r'^login/$', 'profiles.views.login', name="login"),
    url(r'^signup/$', 'profiles.views.signup', name="signup"),
    url(r'^signup/register/$', 'profiles.views.register', name="register"),
    url(r'^dashboard/$', 'profiles.views.dashboard', name="dashboard"),
)


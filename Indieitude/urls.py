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
<<<<<<< HEAD
    url(r'^home/', 'home.views.base', name="base"),
    url(r'^profiles/', 'profiles.views.login', name="login"),
=======
    # url(r'^profiles/', include('profiles.urls')),
    url(r'^$', 'home.views.index'),
    url(r'^likes/', include('likes.urls')),
>>>>>>> FETCH_HEAD
)


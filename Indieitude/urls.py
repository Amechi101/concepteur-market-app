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
    url(r'^home/', 'home.views.base', name="base"),
    url(r'^profiles/', 'profiles.views.login', name="login"),
)


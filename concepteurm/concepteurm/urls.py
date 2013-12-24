from django.conf.urls import patterns, include, url
# from concepteurm import ProfileView
# from django.utils.translation import ugettext as _

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'concepteurm.views.home', name='home'),
    # url(r'^concepteurm/', include('concepteurm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^p_infoapp/', include('p_infoapp.urls')),
    # url(r'^accounts/profile', 'accounts.views.homePage'),
    # url(r'^accounts/signin', include('userena.urls')),
)

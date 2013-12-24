from django.conf.urls import patterns, url

from p_infoapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)

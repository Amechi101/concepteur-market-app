from __future__ import unicode_literals

from django.conf.urls import patterns, url

from designers.views import DesignerListView


urlpatterns = patterns("",
    url(r"^browse/", DesignerListView.as_view(), name="designer_browse"),
)
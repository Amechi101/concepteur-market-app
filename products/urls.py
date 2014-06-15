from __future__ import unicode_literals

from django.conf.urls import patterns, url

from products.views import ProductListView


urlpatterns = patterns("",
    url(r"^browse/", ProductListView.as_view(), name="browse_view"),
)


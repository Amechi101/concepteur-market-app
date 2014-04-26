from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView

from products.models import Product

from django.contrib import admin


urlpatterns = patterns('',
    url(r"^$", ListView.as_view(
    	template_name="homepage.html",
    	model = Product,
    	context_object_name = "product_image",
    	), name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^account/", include("account.urls")),
    url(r'^likes/', include('likes.urls')),
)
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    



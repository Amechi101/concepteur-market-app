from __future__ import unicode_literals

from django.http import Http404, HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.utils.http import base36_to_int, int_to_base36
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.edit import FormView

from django.contrib import auth, messages
from django.contrib.sites.models import get_current_site
from django.shortcuts import render

from products.forms import Product, ProductCategory
from products.forms import Boutique
from products.forms import Designer

from products.models import Boutique, Product, ProductCategory, Designer


from __future__ import unicode_literals

from django.http import Http404, HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import ListView

from django.contrib import auth, messages
from django.contrib.sites.models import get_current_site
from django.shortcuts import render

from designers.forms import Designer

from designers.models import Designer



class DesignerListView(ListView):
	template_name="designers/designer_base.html"
	model = Designer
	context_object_name = "designer_list"

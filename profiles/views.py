#coding=utf-8
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login ,logout as auth_logout
from django.utils.translation import ugettext_lazy as _
from forms import LoginForm
from models import ProfileUser

def login(request):
    template_var={}
    form = LoginForm()    
    if request.method == 'POST':
        form = LoginForm(request.POST.copy())
        if form.is_valid():
            _login(request,form.cleaned_data["username"],form.cleaned_data["password"])
            return HttpResponseRedirect(reverse("login"))
    template_var["form"]=form        
    return render_to_response("registration/login.html",template_var,context_instance=RequestContext(request))


def _login(request,username,password):
    ret = False
    user = authenticate(username=username,password=password)
    if user:
        if user.is_active:
            auth_login(request,user)
            ret=True
        else:
            messages.add_message(request, messages.INFO, _(u'user is not active'))
    else:
        messages.add_message(request, messages.INFO, _(u'user does not exsist'))
    return ret
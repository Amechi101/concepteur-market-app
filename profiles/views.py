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
from forms import LoginForm, SignupForm, RegisterForm
from models import ProfileUser
from PIL import Image


###### Login for users ###########
def login(request):
    template_var={}
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST.copy())
        if form.is_valid():
            login(request,form.cleaned_data["username"],form.cleaned_data["password"])
            return HttpResponseRedirect(reverse("login"))
    template_var["form"]=form
    return render_to_response("registration/login.html",template_var,context_instance=RequestContext(request))

def _login(request,username,password):
    ret=False
    user=authenticate(username=username,password=password)
    if user:
        if user.is_active:
            auth_login(request,user)
            ret=True
        else:
            messages.add_message(request, messages.INFO, _(u'user is not active'))
    else:
        messages.add_message(request, messages.INFO, _(u'user not exsist'))
    return ret


###### Signup for users ###########
def signup(request):
    template_var={}
    form = SignupForm()
    if request.method=="POST":
        form=SignupForm(request.POST.copy())
        if form.is_valid():
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=User.objects.create_user(username,email,password)
            user.save()
            _login(request,username,password)
            return HttpResponseRedirect("register")
    template_var["form"]=form
    return render_to_response("registration/signup.html",template_var,context_instance=RequestContext(request))

###### Registration for users ###########
def register(request):
    template_var={}
    form = RegisterForm()  
    if request.user.is_authenticated():
        if request.method=="POST":
           form=RegisterForm(request.POST,request.FILES)
           if form.is_valid():
                first_name=form.cleaned_data["first_name"]
                last_name=form.cleaned_data["last_name"]
                birthday=form.cleaned_data["birthday"]
                city = form.cleaned_data["city"]
                state = form.cleaned_data["state"]   
                reqfile = request.FILES.get("image", False)
                registeruser=ProfileUser.objects.create(user=request.user, birthday=birthday, user_title='Fashionista', user_points=0,
                    city=city, state=state, image=reqfile)
                registeruser.save()
                return HttpResponseRedirect(reverse("dashboard"))          
        template_var["form"]=form        
        return render_to_response("registration/register.html",template_var,context_instance=RequestContext(request))   


###### Profile for users ###########
def dashboard(request):
    template_var={}
    if request.user.is_authenticated():
        user = ProfileUser.objects.get(user=request.user)
        
        first_name=request.user.first_name
        last_name=request.user.last_name
        email=request.user.email
        username=request.user.username
        birthday=user.birthday
        city=user.city
        state=user.state
        title=user.user_title
        points=user.user_points
        image=user.image.path
        
        #Template 
        template_var["first_name"]=first_name
        template_var["last_name"]=last_name
        template_var["email"]=email
        template_var["username"]=username
        template_var["birthday"]=birthday
        template_var["city"]=city
        template_var["state"]=state
        template_var["title"]=title
        template_var["points"]=points
        template_var["image"]=image
       
        template_var["is_authenticated"]= True
    return render_to_response("userprofile/dashboard.html",template_var, context_instance=RequestContext(request))   
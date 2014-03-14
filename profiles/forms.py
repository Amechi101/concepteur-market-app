#coding=utf-8
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.forms import extras
import time
from models import ProfileUser

now=time.localtime()

class LoginForm(forms.Form):
    username=forms.CharField(label=_(u"username"),max_length=30,widget=forms.TextInput(attrs={'size': 20,}))
    password=forms.CharField(label=_(u"password"),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))


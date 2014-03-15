#coding=utf-8
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.forms import extras
import time
from models import ProfileUser

now=time.localtime()

###### Login for users ###########
class LoginForm(forms.Form):
    username=forms.CharField(label=_(u"username"),max_length=30,widget=forms.TextInput(attrs={'size': 20,}))
    password=forms.CharField(label=_(u"password"),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))

    class Meta:
        """docstring for Meta"""
        model = User


###### Registration for users ###########
class RegisterForm(forms.Form):
    email=forms.EmailField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Email', 'required':True}))    
    username=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Username','required':True}))
    password=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Password','required':True}))
    # password2=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Re-Enter Password','required':True}))
     

    class Meta:
        """docstring for Meta"""
        model = User
        fields = ('email', 'username', 'password', 'password2')

    
    def clean_username(self):
        users = User.objects.filter(username__iexact=self.cleaned_data["username"])
        if not users:
            return self.cleaned_data["username"]
        raise forms.ValidationError(_(u"this username is already exsist"))
        
    def clean_email(self):
        emails = User.objects.filter(email__iexact=self.cleaned_data["email"])
        if not emails:
            return self.cleaned_data["email"]
        raise forms.ValidationError(_(u"this email is already registered"))

    # def clean_password(self):
    #     password = self.cleaned_data.get("password","")
    #     password2 = self.cleaned_data['password2']
    #     if password != password2:
    #         raise forms.ValidationError(_("Password does not match"))




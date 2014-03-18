#coding=utf-8
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.forms import extras
from models import ProfileUser
import time

now=time.localtime()

###### Login for users ###########
class LoginForm(forms.ModelForm):
    username=forms.CharField(label=_(u"username"),max_length=30,widget=forms.TextInput(attrs={'size': 20,}))
    password=forms.CharField(label=_(u"password"),max_length=30,widget=forms.PasswordInput(attrs={'size': 20,}))

    class Meta:
        """docstring for Meta"""
        model = User


###### Signup for users ###########
class SignupForm(forms.ModelForm):
    email=forms.EmailField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Email', 'required':True}))
    username=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Username','required':True}))
    password=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Password','required':True}))
    password2=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder': 'Re-Enter Password','required':True}))
     

    class Meta:
        """ To Specify the fields from User model from django, and to prevent abstraction"""
        model = User
        fields = ['email', 'username', 'password', 'password2']

    
    def clean_username(self):
        users = User.objects.filter(username__iexact=self.cleaned_data["username"])
        if not users:
            return self.cleaned_data["username"]
        raise forms.ValidationError("This username already exist")
        
    def clean_email(self):
        emails = User.objects.filter(email__iexact=self.cleaned_data["email"])
        if not emails:
            return self.cleaned_data["email"]
        raise forms.ValidationError("Email is already registered")

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if not password2:
            raise forms.ValidationError("You must confirm your password")

        if password != password2:
            raise forms.ValidationError("The password does not match ")

        return password2

###### Registration for users ###########
class RegisterForm(forms.ModelForm):
    first_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'First Name','required':True}))
    last_name=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Last Name','required':True}))
    birthday=forms.DateField(label=_(u"birthdate(mm/dd/yy)"),widget=extras.SelectDateWidget(years=range(1900, now[0]+1)),required=False)
    city=forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'City','required':True}))
    state=forms.CharField(max_length=2, widget=forms.TextInput(attrs={'placeholder': 'State','required':True}))
    image = forms.ImageField(required=False)

    class Meta:
        """ To Specify the fields from User model and the extension of the user model from django, and to prevent abstraction"""
        model = ProfileUser
        fields = ['first_name','last_name', 'birthday','city','state','image']


    
    


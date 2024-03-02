#Inherits from our usercreationform and used to add more fields like email, etc
#Corey's Djano series part 6 second last part!

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        #nested name space for configs and keeps them in one place
        #model that will be affected will be User model, and on form.save it will save it to User model
        #the model is a user and gets validated thru it? ig?
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        #nested name space for configs and keeps them in one place
        #model that will be affected will be User model, and on form.save it will save it to User model
        #the model is a user and gets validated thru it? ig?
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
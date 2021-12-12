from django import forms 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    SEX = (
    ('F','Female'),
    ('M','Male'),
    ('U','Other'),
    )
    
    email = forms.EmailField(max_length=200, help_text='Required')
    sex = forms.ChoiceField(choices= SEX)
    
    
    class Meta:
        
        model = User
        fields = ["username","sex","email","password1","password2"]
        

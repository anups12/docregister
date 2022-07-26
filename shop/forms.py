from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Doctor, Post


class UserCreate(UserCreationForm):
    class Meta:
        model = User
        fields=('username','first_name', 'last_name', 'email', 'password1', 'password2')
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Unique username'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Enter Password'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirm Password'}),
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter first name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter last name'}),
        }
    

class AddPost(forms.ModelForm):
    class Meta:
        model = Post
        fields='__all__'
        exclude = ['user']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Title'}),
            'summary':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter Summary', 'rows':'5'}),
            'content':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Content'}),
            'image':forms.FileInput(attrs={'class':'form-control'}),   
        }
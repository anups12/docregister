from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Doctor, Patient


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
    

class UpdateCustomer(forms.ModelForm):
    class Meta:
        model = Doctor
        fields='__all__'
        exclude = ['user']
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter name'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Enter Email'}),
            'phone':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Enter Phone Number '}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}),
            'pin':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Pincode'}),
            'city':forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}),
            'state':forms.TextInput(attrs={'class':'form-control', 'placeholder':'State'}),
            'pic':forms.FileInput(attrs={'class':'form-control', 'placeholder':'State'}),
        }
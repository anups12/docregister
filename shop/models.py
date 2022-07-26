from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Doctor(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    address = models.CharField(max_length=100,default=None,null=True,blank=True)
    pin = models.CharField(max_length=50,default=None,null=True,blank=True)
    city = models.CharField(max_length=50,default=None,null=True,blank=True)
    state = models.CharField(max_length=50,default=None,null=True,blank=True)
    pic = models.ImageField(upload_to='images',default='avatar.jpg',null=True,blank=True)
    def __str__(self):
        return str(self.first_name)



class Patient(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    address = models.CharField(max_length=100,default=None,null=True,blank=True)
    pin = models.CharField(max_length=50,default=None,null=True,blank=True)
    city = models.CharField(max_length=50,default=None,null=True,blank=True)
    state = models.CharField(max_length=50,default=None,null=True,blank=True)
    pic = models.ImageField(upload_to='images',default='avatar.jpg',null=True,blank=True)
    def __str__(self):
        return str(self.first_name)


CATEGORY_CHOICES=(
    ('Mental Health', 'mental helath'),
    ('Heart Disease', 'heart disease'),
    ('Lungs Disease', 'lungs disease'),
    ('Fracture', 'fracture'),
)

class Post(models.Model):
    user= models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    image= models.ImageField(upload_to='images', null=True, blank=True)
    category= models.CharField(choices=CATEGORY_CHOICES, max_length=30)
    summary=models.TextField()
    content= models.CharField(max_length=200)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title
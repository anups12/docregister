from django.contrib import admin
from . models import Doctor, Patient, Post

# Register your models here.
@admin.register(Doctor)
class CustomerRegister(admin.ModelAdmin):
    model=Doctor
    list_display=('username','first_name','last_name' ,'email', 'pic')

@admin.register(Patient)
class CustomerRegister(admin.ModelAdmin):
    model=Patient
    list_display=('username','first_name','last_name' ,'email', 'pic')

@admin.register(Post)
class CustomerRegister(admin.ModelAdmin):
    model=Post
    list_display=('user','title','category')
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home, name='home'),
    path('register/',views.Create_User, name='register'),
    path('login/',views.CustomerLogin, name='login'),
    path('logout/',views.UserLogout, name='logout'),
    path('profile/',views.Profile, name='profile'),
    path('create/',views.CreatePost, name='create'),

]
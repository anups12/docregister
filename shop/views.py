from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Doctor, Patient, Post
from . forms import UserCreate, AddPost
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def Home(request):
    mh = Post.objects.filter(draft=False , category='Mental Health')
    hd = Post.objects.filter(draft=False , category='Heart Disease')
    ld = Post.objects.filter(draft=False , category='Lungs Disease')
    fc = Post.objects.filter(draft=False , category='Fracture')
    try:
        doctors_post= Post.objects.filter(user=request.user.doctor)
    except:
        doctors_post={}
    context={'mh':mh, 'doctors_post':doctors_post, 'hd':hd, 'ld':ld,'fc':fc}
    return render(request, 'home.html', context)
    

def CreatePost(request):
    form = AddPost()
    if request.method=='POST':
        form = AddPost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user=request.user.doctor
            instance.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'create.html', context)
    

def Profile(request):
    if request.user.is_superuser:
        data={}
    elif not request.user.is_authenticated:
        data={}
    else:
        try:
            if request.user.doctor:
                data=Doctor.objects.get(username=request.user)
        except:
            data=Patient.objects.get(username=request.user)
    context={'data':data}
    return render(request, 'profile.html', context)


def Create_User(request):
    form = UserCreate()
    if request.method=='POST':
        radio= request.POST.get('radio')
        address= request.POST.get('address')
        city= request.POST.get('city')
        state= request.POST.get('state')
        pincode= request.POST.get('pincode')
        image= request.FILES.get('image')
        print(radio, address, city, state, pincode,image)
        form = UserCreate(request.POST)
        if form.is_valid():
            user = form.save()
            if radio=='doctor':
                Doctor.objects.create(first_name=user.first_name,last_name=user.last_name, email=user.email, username=user, address=address, city=city, state=state, pin=pincode, pic=image)
                print("doctor worked")
                messages.success(request, 'User created Successfully  '+ user.first_name + " " +user.last_name)
            elif radio=='patient':
                Patient.objects.create(first_name=user.first_name,last_name=user.last_name, email=user.email, username=user, address=address, city=city, state=state, pin=pincode, pic=image)
                print("patient worked")
                messages.success(request, 'User created Successfully  '+ user.first_name + " " +user.last_name)
            return redirect('/login/')
    context={'form':form}
    return render(request, 'register.html', context)

def CustomerLogin(request): 
    form = UserCreate()
    context={'form':form}
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user) 
                messages.success(request, 'User Logged in Successfully as  '+ user.first_name + " " +user.last_name)
                try:
                    if request.user.customer:
                        return redirect('/')
                except:
                    return redirect('/login/')
            else:
                messages.warning(request, "Either your username or password is wrong")
    return render(request, 'register.html', context)



def UserLogout(request):
    logout(request)
    messages.warning(request, 'Your have logged out  ')
    return redirect('/login/')
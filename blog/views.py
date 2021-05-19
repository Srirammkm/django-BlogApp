from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .models import *
from .form import *

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('/login/')
    else:
        #form = CreateUserForm()
        form = UserForm()
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/login')
        context = {'form': form}
        return render(request,'blog/register.html',context)
    
def view_login(request):
    if request.user.is_authenticated:
        return redirect('/login/')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            for uname in PUser.objects.all():
                if username == uname.username and password == uname.password:
                    return redirect(f'/home/{ uname.id }')         
                else:
                    messages.info(request, 'Username OR password is incorrect')
                
        context = {}
        return render(request,'blog/login.html',context)

def logoutuser(request):
    logout(request)
    return redirect('/login')


def home(request,pk):
    posts = Post.objects.all().order_by('-date')
    users = PUser.objects.all()
    pk = pk
    return render(request,'blog/feed.html',{'posts': posts , 'users': users, 'pk':pk})


def profile(request,pk,up):
    try:
        posts = Post.objects.all().filter(user=up)
        users = PUser.objects.all()
        user = PUser.objects.get(id=up)
        pk = pk
        return render(request,'blog/profile.html',{'posts': posts, 'user': user,'pk':pk, 'users': users})
    except :
        user = {'name':"No User found"}
   
        return render(request,'blog/profile.html',{'user': user})


def createpost(request,pk):
    users = PUser.objects.all()
    user = PUser.objects.get(id=pk)
    form = PostForm(initial={'user': user})
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/home/{ pk }')
    pk = pk

    context = {'form': form, 'pk':pk , 'users':users}
    return render(request,'blog/post.html',context)


def editprofile(request,pk):
    user = PUser.objects.get(id=pk)
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect(f'/home/{ pk }')
    pk = pk
    context = {'form': form,'pk': pk}
    return render(request,'blog/edit.html',context)

def deletepost(request,pk , pi):
    posts = Post.objects.get(id=pi)
    if request.method == 'POST':
        posts.delete()
        return redirect(f'/home/{ pk }')  
    pk = pk
    return render(request,'blog/postdelete.html',{'pk':pk, 'pi':pi})  

def editpost(request, pk,pi):
    post = Post.objects.get(id=pi)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect(f'/home/{ pk }')
    pk = pk
    return render(request,'blog/editpost.html',{'form':form, 'pi':pi,'pk':pk,})



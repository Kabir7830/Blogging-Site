from django.contrib import messages
import datetime
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from blogs.models import User_Blogs
User = get_user_model()
# Create your views here.


def Create_User(request):
    if request.user.is_authenticated:
        return redirect("/user")
    if request.method =="POST":

        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']

        user = User.objects.create_user(username=username,email=email,password=password)
        login(request,authenticate(request,email=email,password=password))
        messages.success(request,f"{str(request.user.username).upper()}, Welcome to Blogging Spot")
        return redirect("/user")
    return render(request,"index.html")



def Login_Handler(request):

    if request.user.is_authenticated:
        return redirect("/user")
    if request.method=="POST":

        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,username=email,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f"Welcome, {str(request.user.username).upper()}")
            return redirect("/user")
    messages.error(request,"Wrong Email or Password !")
    return redirect("/")



def Logout_Handler(request):

    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"Logged Out")
        return redirect("/")
    messages.error(request,"Please Login!")
    return redirect("/")



def Show_Dashboard(request):
    if "search" in request.GET:
        query = request.GET['search']
        posts = User_Blogs.objects.filter(user_id = request.user.id).filter(blog_title__icontains = query)
        return render(request,"posts.html",{"posts":posts})
    posts = User_Blogs.objects.filter(user_id = request.user.id)
    user = User.objects.filter(id = request.user.id)
    return render(request,"posts.html",{"posts":posts})

def edit_post(request,blog_id):

    blog = User_Blogs.objects.filter(id = blog_id).first()
    if request.method == "POST":

        blog.blog_title = request.POST['blog_title']
        blog.blog_description = request.POST['blog_description']
        blog.published = request.POST['blog_published']
        blog.modified_date = datetime.date.today()
        try:
            blog.save()
            messages.success(request,"Updation Success")
            return redirect("/user")
        except Exception as e:
            messages.error(request,"Something Went Wrong! Try Again")
            return("/user")
    return render(request,"edit_blog.html",{"post":blog})


def Delete_Post(request,blog_id):

    if request.method == "POST":
        blog = User_Blogs.objects.filter(id = blog_id).first()
        blog.delete()
        messages.success(request,"Deleted Sucessfully")
        return redirect("/user")
    return render(request,"confirm_delete.html")


def Direct_Login(request,email,password):

    user = authenticate(request,email=email,password=password)
    login(request,user)
    messages.success(request,"Welcome to Blogging Spot")
    return render(request,"posts.html")


def Delete_User(request,user_id):

    if request.method == "POST":

        user = User.objects.filter(id = user_id).first()
        blogs = User_Blogs.objects.filter(user_id = user_id)
        blogs.delete()
        user.delete()
        messages.success(request,"Deleted Successfully")
        return redirect("/")
    return render(request,"confirm_delete.html")
    

def User_Settings(request,user_id):
    
    user = User.objects.filter(id = user_id).first()
    if request.method == "POST":

        email = request.POST['email']
        user.email = email
        user.save()
        messages.success(request,"updation Success")
        return redirect("/user")
    return render(request,"edit_user.html",{"user":user})
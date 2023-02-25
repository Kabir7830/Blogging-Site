from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
import datetime


def display_home(request):
    if request.user.is_authenticated:
        return redirect("/user")
    return render(request,"index.html")


def Create_New_Blog(request):
    
    if request.method == "POST":
        blog_title = request.POST["blog_title"]
        blog_description = request.POST["blog_description"]
        made_date = datetime.date.today()
        published = True
        new_blog = User_Blogs.objects.create(blog_title=blog_title,
                                            blog_description=blog_description,
                                            made_date=made_date,
                                            published=published,
                                            user_id_id=request.user.id)
        messages.success(request,"Blog Posted")
        return redirect("/user")
        
    return render(request,"create_new_blog.html")

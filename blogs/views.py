from django.shortcuts import render

# Create your views here.


def display_home(request):
    return render(request,"index.html")
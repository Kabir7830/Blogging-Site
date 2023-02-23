from django.urls import path
from . import views
urlpatterns = [
    path("",views.display_home),
    path("new-blog",views.Create_New_Blog),
]

from django.urls import path
from . import views

urlpatterns = [
    path("signup",views.Create_User),
    path("login",views.Login_Handler),
    path("logout",views.Logout_Handler),
    path("",views.Show_Dashboard),
    path("blog/<int:blog_id>",views.edit_post),
    path("blog/<int:blog_id>/delete",views.Delete_Post),
    path("<int:user_id>/settings",views.User_Settings),
    path("<int:user_id>/delete",views.Delete_User),
]

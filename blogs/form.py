from django import forms
from .models import *


class User_Blogs_Form(forms.ModelForm):

    class Meta:
        model = User_Blogs
        fields = [
            "blog_title",
            "blog_description",
            "made_date",
            "modified_date",
            "published",
        ]
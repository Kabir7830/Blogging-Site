from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class User_Blogs(models.Model):

    class Meta:
        db_table = "User_Blogs"


    blog_title = models.CharField(max_length=60)
    blog_description = models.TextField()
    made_date = models.DateField(blank=True,null=True)
    modified_date = models.DateField(blank=True,null=True)
    published = models.BooleanField(default=True, blank=True, choices=((True,'True'),(False,'False')))
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)


from django.db import models

# Create your models here.

class User_Blogs(models.Model):

    blog_title = models.CharField(max_length=60)
    blog_description = models.TextField()
    made_date = models.DateField()
    modified_date = models.DateField(blank=True,null=True)
    published = models.BooleanField(default=True, blank=True, choices=((True,'True'),(False,'False')))
    
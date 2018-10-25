from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Media(models.Model):
    name    = models.CharField(max_length=30)
    video   = models.CharField(max_length=30)
    image   = models.CharField(max_length=30)
    text 	= models.CharField(max_length=30)

class Article(models.Model):
	title 		= models.CharField(max_length=30)
	content 	= models.CharField(max_length=30)
	media  		= models.ManyToManyField(Media)

class MemberGroup(models.Model):
    name   		= models.CharField(max_length=30)
    members 	= models.ManyToManyField(User)
    articles	= models.ManyToManyField(Article)
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe
from django.conf import settings

# Create your models here.
class Media(models.Model):
    name    = models.CharField(max_length=30)
    video   = models.FileField(upload_to='videos', null=True, blank=True)
    image   = models.ImageField(upload_to='images', null=True, blank=True )
    text 	= models.CharField(max_length=1000, null=True, blank=True)
    def image_tag(self):
        return mark_safe('<img src="/musicschool/media/%s" width="500" height="auto" />' % (self.image))
    image_tag.short_description = 'Image'

    def __str__(self):
        return self.name

    def image_url(self):
        return ("/musicschool/media/%s" % (self.image))

class Article(models.Model):
    title 		= models.CharField(max_length=30)
    content 	= models.CharField(max_length=300)
    media  		= models.ManyToManyField(
        Media, 
        related_name='media',
        blank=True
    )

    def __str__(self):
        return self.title


class MemberGroup(models.Model):
    name   		= models.CharField(max_length=30)
    members 	= models.ManyToManyField(User, related_name='members_group')
    articles	= models.ManyToManyField(Article, related_name='articles_group')

    def __str__(self):
        return self.name


class UserInformations(models.Model):
    phonenumber	= models.CharField(max_length=30)
    adress      = models.CharField(max_length=50)
    user 	= models.OneToOneField(
        User, 
        related_name='user_information',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return  '%s %s' % (self.user.firstname,self.user.lastname)
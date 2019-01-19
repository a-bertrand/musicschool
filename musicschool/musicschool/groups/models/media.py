from markdownx.models import MarkdownxField
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Media(models.Model):
    name    = models.CharField(max_length=30)
    video   = models.FileField(upload_to='videos', null=True, blank=True)
    image   = models.FileField(upload_to='images', null=True, blank=True )
    text 	= MarkdownxField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.name

    def image_url(self):
        return ("/musicschool/media/%s" % (self.image))
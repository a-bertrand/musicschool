from markdownx.models import MarkdownxField
from django.db import models
from django.contrib.auth.models import User
from .article import Article

class MemberGroup(models.Model):
    name   		= models.CharField(max_length=30)
    members 	= models.ManyToManyField(User, related_name='members_group')
    articles	= models.ManyToManyField(Article, related_name='articles_group')

    def __str__(self):
        return self.name

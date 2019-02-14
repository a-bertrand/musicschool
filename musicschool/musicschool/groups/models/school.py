from django.db import models
from django.contrib.auth.models import User
from .article import Article
from .media import Media
from .membergroup import MemberGroup
from .userinformation import ERPUser
from .category import Category


class School(models.Model):
    name 		= models.CharField(max_length=30)
    address     = models.CharField(max_length=50)
    phone       = models.CharField(max_length=20)
    article     = models.ManyToManyField(
        "Article", 
        verbose_name=_("Articles")
    )
    group       = models.ManyToManyField(
        "Group", 
        verbose_name=_("Groupes")
    )
    media       = models.ManyToManyField(
        "Media", 
        verbose_name=_("Médias")
    )


class SchoolRight(models.Model):
    PROF    = 'Prof'
    STUDENT = 'Student' 
    LEVEL_USER_CHOICES = (
        (PROF, PROF),
        (STUDENT, STUDENT)
    )
    
    ERPUser =   models.models.ForeignKey(
        ERPUser, 
        on_delete=models.CASCADE)() 
    ) 
    School  =   models.models.ForeignKey(
        School, 
        on_delete=models.CASCADE)() 
    )    
    Level   =   models.CharField(
        max_length=20, 
        choices=LEVEL_USER_CHOICES, 
        default=STUDENT
    )

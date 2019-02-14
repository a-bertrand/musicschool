from django.db import models
from django.contrib.auth.models import User


class ERPUser(models.Model):
    phonenumber	= models.CharField(max_length=30)
    adress      = models.CharField(max_length=50)
    user    = models.OneToOneField(
        User, 
        related_name='user_information',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    def __str__(self):
        return  '%s %s' % (self.user.first_name,self.user.last_name)

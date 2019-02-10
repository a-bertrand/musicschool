from django.db import models
from django.contrib.auth.models import User

class UserInformations(models.Model):
    phonenumber	= models.CharField(max_length=30)
    adress      = models.CharField(max_length=50)
    is_prof     = models.BooleanField(default=False)
    user 	    = models.OneToOneField(
        User, 
        related_name='user_information',
        on_delete=models.CASCADE
    )
    prof = models.OneToOneField(
        User, 
        related_name='user_information',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return  '%s %s' % (self.user.firstname,self.user.lastname)

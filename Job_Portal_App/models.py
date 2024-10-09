from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User_Model(AbstractUser):

    TYPE = [
        ('job seeker', 'Job Seeker'),
        ('recruiter', 'Recruiter')
    ]

    user_type = models.CharField(choices=TYPE, max_length=50, null=True)

    
    
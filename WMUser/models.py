from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import datetime

# Create your models here.
class WMUser(AbstractBaseUser):
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

	birthdate = models.DateField(default=datetime.date(1900,1,1), blank=True, null=True)
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
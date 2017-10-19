from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class WMUser(User):
	class Meta:
		proxy = True
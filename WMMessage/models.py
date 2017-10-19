from django.db import models
from WMUser.models import *
import datetime

# Models for Messaging
class WMMessage(models.Model):
     sender = models.ForeignKey(WMUser, related_name="sender")
     receiver = models.ForeignKey(WMUser, related_name="receiver")
     message = models.CharField(max_length=99999)
     created_at = models.DateField(default=datetime.date.today)

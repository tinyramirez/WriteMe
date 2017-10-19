from django.db import models
from WMUser.models import *
import datetime

# Create your models here.
class WMMessage(models.Model):
     sender = models.ForeignKey(WMUser, related_name="sender")
     reciever = models.ForeignKey(WMUser, related_name="receiver")
     msg_content = models.CharField(max_length=99999)
     created_at = models.DateField(default=datetime.date.today)

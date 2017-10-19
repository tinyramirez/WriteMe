from django.shortcuts import render
from django.views.generic import ListView	
from WMMessage.models import WMMessage

# Create your views here.
class WMMessageList(ListView):
    model = WMMessage
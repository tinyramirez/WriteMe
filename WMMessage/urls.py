# urls.py
from django.conf.urls import url
from WMMessage.views import WMMessageList

urlpatterns = [
    url(r'^messages/([\w-]+)/$', WMMessageList.as_view()),
]
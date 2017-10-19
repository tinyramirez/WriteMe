# urls.py
from django.conf.urls import url
from WMMessage.views import *

app_name = 'WMMessage'

urlpatterns = [
    url(r'^view/$', WMMessageList.as_view()),
    url(r'^new/$', NewMessageView.as_view()),
    url(r'^thread/(?P<pk>[0-9]+)/$', MessageThreadView.as_view(), name='messages_thread'),
]
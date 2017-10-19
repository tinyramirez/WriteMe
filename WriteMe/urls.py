"""WriteMe URLs
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^messages/', include('WMMessage.urls', namespace='WMMessage')),
    url(r'^user/', include('WMUser.urls', namespace='WMUser')),
]

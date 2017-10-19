from django.conf.urls import url
from django.contrib.auth import views as auth_views
from WMUser.views import *

app_name = 'WMUser'

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'login.html' }, name='login'),
	url(r'^logout/$', LogoutView.as_view(), name='logout'),   
	url(r'^signup/$', SignupView.as_view(), name='signup'),
    url(r'^home/$', WMUserList.as_view(), name='home'),	
]
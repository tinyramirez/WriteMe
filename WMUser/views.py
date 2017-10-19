from django.shortcuts import render,redirect
from WMUser.models import WMUser
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from WMUser.forms import *

# Create your views here.
class WMUserList(View):
    def get(self, request):
        users = WMUser.objects.all()
        user_dict = {}
        for user in users:
            user_dict[user] = '/messages/thread/'+str(user.pk)+'/'
        return render(request, 'userlist.html', {'users': users, 'user_url':user_dict, 'current': request.user}) 

class SignupView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form}) 

    def post(self, request):
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('/user/home/')
        else:
            form = SignUpForm()
        return render(request, 'signup.html', {'form': form}) 

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/user/login/')

    def post(self, request):
        logout(request)
        return redirect('/user/login/')
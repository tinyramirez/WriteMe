from django.shortcuts import render, redirect
from django.views.generic import View	
from WMMessage.models import WMMessage
from WMUser.models import WMUser
from WMMessage.forms import MessageForm, MessageListForm
from itertools import chain
from operator import attrgetter

# Create your views here.
class WMMessageList(View):
	def get(self, request):
		messages = WMMessage.objects.all()
		return render(request, 'messages.html')

class NewMessageView(View):
	def get(self,request):
		form = MessageForm(initial={'sender': request.user})
		return render(request, 'new_message.html', {'form': form, 'current': request.user}) 

	def post(self, request):
		if request.method == 'POST':
			form = MessageForm(request.POST)
			if form.is_valid():
				message = form.save()
				receiver = form.cleaned_data['receiver']
				user = WMUser.objects.get(username=receiver)
				return redirect('/messages/thread/'+str(user.pk)+'/')
		else:
			form = MessageForm(initial={'sender': request.user})
		return render(request, 'new_message.html', {'form': form, 'current': request.user})

class MessageThreadView(View):
	def get(self,request, pk):
		messages1 = WMMessage.objects.filter(sender_id=pk, receiver_id=request.user.pk)
		messages2 = WMMessage.objects.filter(receiver_id=pk, sender_id=request.user.pk)

		messages = sorted(list(chain(messages1, messages2)), key=attrgetter('created_at'))
		receiver = WMUser.objects.get(pk=pk)

		form = MessageListForm(initial={'sender': request.user, 'receiver': receiver})
		return render(request, 'messagelist.html', {'messages': messages, 'current': request.user, 'form': form})

	def post(self, request, pk):
		if request.method == 'POST':
			messages1 = WMMessage.objects.filter(sender_id=pk, receiver_id=request.user.pk)
			messages2 = WMMessage.objects.filter(receiver_id=pk, sender_id=request.user.pk)

			messages = sorted(list(chain(messages1, messages2)), key=attrgetter('created_at'))
			receiver = WMUser.objects.get(pk=pk)

			form = MessageListForm(request.POST)
			if form.is_valid():
				message = form.save()
				return redirect('/messages/thread/'+str(pk)+'/')
		else:
			form = MessageListForm(initial={'sender': request.user, 'receiver': receiver})
		return render(request, 'messagelist.html', {'messages': messages, 'current': request.user, 'form': form})
		




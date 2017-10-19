from django import forms
from django.forms import ModelForm
from WMMessage.models import WMMessage

class MessageForm(ModelForm):
    class Meta:
        model = WMMessage
        fields = ('sender','receiver', 'message')
        widgets = {
            'sender': forms.HiddenInput(),
            'message': forms.TextInput(),
        }

class MessageListForm(ModelForm):
    class Meta:
        model = WMMessage
        fields = ('sender','receiver', 'message')
        widgets = {
            'sender': forms.HiddenInput(),
            'receiver': forms.HiddenInput(),
        }
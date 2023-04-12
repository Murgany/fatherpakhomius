from django import forms 
from .models import UserMessage


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)


class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ('subject', 'email_address', 'message')
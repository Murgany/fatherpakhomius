from django import forms 
from .models import UserMessage


# Usr message form | Contact us page

class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ('subject', 'email_address', 'message')

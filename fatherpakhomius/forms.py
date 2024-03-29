from django import forms 
from .models import UserMessage


# User message form | Used in Contact us page

class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ('subject', 'email_address', 'message')

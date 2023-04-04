from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)

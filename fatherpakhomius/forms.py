from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit


class ContactForm(forms.Form):
    # name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    email_address = forms.EmailField(max_length=150)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)


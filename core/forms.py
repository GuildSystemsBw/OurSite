from django import forms

class ContactForm(forms.Form):
    email = forms.CharField(required=True, widget=forms.widgets.EmailInput(attrs={'placeholder': 'Your email...', 'class': 'form-control mb-4'}))
    subject = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Subject...', 'class': 'form-control mb-4'}))
    content = forms.CharField(required=True, widget=forms.widgets.Textarea(attrs={'placeholder': 'Your message...', 'class': 'form-control mb-4','rows':'6'}))
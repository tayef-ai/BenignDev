from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['cname', 'phone', 'email', 'message']
        labels = {
            'cname': 'Name',
        }
        widgets = {
            'cname': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Phone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'How can we help you?', 'style':'height:150px;'}),
        }
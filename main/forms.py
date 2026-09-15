from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'number', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control ps-3 me-3'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control ps-3'
            }),
            'number': forms.TextInput(attrs={
                'class': 'form-control ps-3'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control ps-3'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control ps-3'
            })
        }
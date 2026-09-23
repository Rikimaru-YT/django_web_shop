from django import forms
from .models import ContactMessage, ProductComment


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'number', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control ps-3 me-3',
                'placeholder': 'Write your name here'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control ps-3',
                'placeholder': 'Write your email here'
            }),
            'number': forms.TextInput(attrs={
                'class': 'form-control ps-3',
                'placeholder': 'Write your phone number here'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control ps-3',
                'placeholder': 'Write your subject here'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control ps-3',
                'placeholder': 'Write your message here'
            })
        }

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['review']
        widgets = {
            'review': forms.Textarea(attrs={'class': 'form-control ps-3'}),
        }
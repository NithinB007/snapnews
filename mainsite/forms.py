from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'mobile', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your full name', 'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Enter your mobile number', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Enter your message', 'class': 'form-control', 'rows': 5}),
        }

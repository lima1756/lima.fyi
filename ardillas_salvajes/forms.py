from django import forms
from .models import Contact, Comment

class ContactForm(forms.ModelForm):
    """
        This form is the representation of the Model Contact
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'content']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    """
        This form is the representation of the Model Comment
    """
    class Meta:
        model = Comment
        fields = ['name', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
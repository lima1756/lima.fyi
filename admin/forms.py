from django import forms
from .models import ResumeLog

class ResumeLogForm(forms.ModelForm):
    """
        This form is the representation of the Model ResumeLog
    """
    class Meta:
        model = ResumeLog
        fields = ['title', 'description', 'resume']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'resume': forms.HiddenInput(),
        }
        help_texts = {
            'title': 'Short description of the changes (50 chars max)',
            'description': 'Explain all you want about the changes did to the JSON',
        }
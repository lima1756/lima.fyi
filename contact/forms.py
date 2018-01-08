from django import forms
from .models import ContactData

class ContactForm(forms.ModelForm):
    """
        This form is the representation of the Model ContactData
    """
    description = ('This form is for simplify the contact with me instead '
                   'of creating an email or messaging or other method with the '
                   'data in the resume.<br> You only need to fill this and I '
                   'will contact you as soon as I can to the mail you provide.')
    class Meta:
        model = ContactData
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
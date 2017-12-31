from django import forms
from .models import ResumeLog
from blog.models import Post


class ModDateInput(forms.DateInput):
    """
        A modified input based in Date input that generates directly a date input in the web browser instead of a text field
    """
    input_type='date'


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


class PostForm(forms.ModelForm):
    """
        This form is the representation of the Model Blog.Post
    """
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'tags', 'visible']
        widgets = {
            'id': forms.TextInput(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.HiddenInput(),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'visible': forms.CheckboxInput(attrs={'class':'form-check-input', 'style':'margin-top:0.44rem;margin-left:0;'})
        }
        help_texts = {
            'visible': 'If you check it, the post will be visible to the users in the blog. In other hand, if you not check it, the post will not be visible.',
        }

from django import forms
from .models import ResumeLog
from blog.models import Post
from portfolio.models import Project

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
        fields = ['id', 'title', 'content', 'tags', 'visible', 'date_published']
        widgets = {
            'id': forms.TextInput(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.HiddenInput(),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'visible': forms.CheckboxInput(attrs={'class':'form-check-input', 'style':'margin-top:0.44rem;margin-left:0;'}),
            'date_published': ModDateInput
        }
        help_texts = {
            'visible': 'If you check it, the post will be visible to the users in the blog. In other hand, if you not check it, the post will not be visible.',
            'date_published': 'The date you want it to be published, if not setted it will never be visible to the users'
        }



class ProjectForm(forms.ModelForm):
    """
        This form is the representation of the Model Portfolio.Project
    """
    class Meta:
        model = Project
        fields = ['id', 'name', 'summary', 'content', 'logo', 'tags', 'visible']
        widgets = {
            'id': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
            'content': forms.HiddenInput(),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'visible': forms.CheckboxInput(attrs={'class':'form-check-input', 'style':'margin-top:0.44rem;margin-left:0;'})
        }
        help_texts = {
            'visible': 'If you check it, the project will be visible to the users in the portfolio. In other hand, if you not check it, the project will not be visible.'
        }
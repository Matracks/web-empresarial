from django import forms
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',
                                            'placeholder': 'Titulo'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

        labels = {
            'title': '', 'content': ''
        }
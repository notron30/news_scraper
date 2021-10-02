from django import forms
from .models import BlogModel


class BlogModelForm(forms.ModelForm):
    class Meta:
        model= BlogModel
        fields = ['title','content','method']
        widgets = {
        'title': forms.TextInput(attrs = {'class':'form-control',}),
        'content': forms.Textarea(attrs = {'class':'form-control'}),
        'method': forms.Select(attrs={'class':'form-control'}),
        }
        
         
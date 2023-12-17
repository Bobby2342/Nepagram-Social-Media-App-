from django import forms
from .models import Comment 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2}),
        }

from django import forms

class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}))
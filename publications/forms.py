from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_text', ]
        widgets = {
            'comment_text': forms.Textarea(
                attrs={
                    'class': 'contact_input contact_textarea',
                }
            )
        }

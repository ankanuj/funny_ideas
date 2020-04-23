from django import forms
from .models import *


class CommentForm(forms.FormModel):
    class Meta:
        model = Comment
        fields = ('comment',)
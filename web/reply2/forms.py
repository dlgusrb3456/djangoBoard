from django import forms

from reply2.models import Reply

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('contents','writer')
        exclude = ('writer',)
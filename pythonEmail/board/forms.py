from django import forms

from board.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post #모델이란 데이터 저장소
        fields = ('title','contents',)
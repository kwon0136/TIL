from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(attrs={
            'class':'title',
            'placeholder':'Enter the title'
        })
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(attrs={
            'class':'content-type',
            'rows':5,
            'cols':50,
            'placeholder':'Enter the content'
        })
    )
    class Meta:
        model = Board
        fields = ['title', 'content',]



# class BoardForm(forms.Form):s
#     title = forms.CharField(
#         max_length=10,
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class':'title',
#                 'placeholder':'Enter the title',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class':'content-type',
#                 'rows':5,
#                 'cols':50,
#                 'placeholder':'Enter the content',
#             }
#         )
#     )
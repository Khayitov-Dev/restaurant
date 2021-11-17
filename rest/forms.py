from django import forms
from .models import Comment

class EmailPost(forms.Form):
    name = forms.CharField(max_length=255)
    Email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False,widget=forms.Textarea)




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body']

class SearchForm(forms.Form):
    q = forms.CharField(max_length=255, label="", widget=forms.TextInput(attrs={"placeholder": "search"}))
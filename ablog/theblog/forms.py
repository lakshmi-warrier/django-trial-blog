from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'body', 'pub_date')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title tag here'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter body here'}),
            'pub_date': forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Enter date here'}),
        }
from django import forms
from .models import BlogPost


class PostForm(forms.Form):
    title = forms.CharField(min_length=5, max_length=30)
    content = forms.CharField(widget=forms.Textarea, min_length=10)


class PostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        qs = BlogPost.objects.filter(title__iexact=title)
        if self.instance is not None:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise forms.ValidationError("This title has already been used. Please try another")
        return title

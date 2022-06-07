from dataclasses import field, fields
from pyexpat import model
from django import forms
from blog.models import Contact

class ContactForm(forms.Form):
    first_name = forms.CharField(min_length=3, max_length=30)
    last_name = forms.CharField(min_length=3, max_length=30)
    email = forms.EmailField(min_length=5, max_length=50)
    subject =  forms.CharField(min_length=10, max_length=150)
    message = forms.CharField(widget=forms.Textarea)

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name','last_name','email','subject','message']
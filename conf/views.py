from django.http import HttpResponse
from django.shortcuts import render

from .form import ContactModelForm
from blog.models import Contact


def home(request):
    return render(request, "index.html")


def about(request):
    return HttpResponse("<h1>Hello World</h1>")


def contact(request):
    form = ContactModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = ContactModelForm()

    context = {
        "form": form
    }
    return render(request, "contact.html", context)

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.shortcuts import render, get_object_or_404, redirect

from .models import BlogPost
from .form import PostModelForm


# Create your views here.


def list(request):
    template = 'list.html'
    list = BlogPost.objects.all()
    context = {'objects': list}
    return render(request, template, context)


@login_required
def create_view(request):
    template = 'create.html'

    form = PostModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        post = form.save(commit=False)
        post.user = request.user
        post.slug = form.cleaned_data.get('title').lower().replace(" ", "-")
        post.save()
        form = PostModelForm()

    context = {'form': form}
    return render(request, template, context)


def detail(request, slug):
    template = 'detail.html'
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj}
    return render(request, template, context)


def update_view(request, slug):
    template = 'update.html'
    post = get_object_or_404(BlogPost, slug=slug)
    form = PostModelForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()

    context = {
        "form": form,
        "title": f"Update {post.title}"
    }
    return render(request, template, context)


@staff_member_required
def delete_view(request, slug):
    template = 'delete.html'
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect("/")

    context = {"post": post}
    return render(request, template, context)

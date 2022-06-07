from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL


# Create your models here.

class BlogPost(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, max_length=50)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.title

    def get_post_url(self):
        return f"{self.slug}/"

    def get_edit_url(self):
        return f"/{self.slug}/edit"

    def get_delete_url(self):
        return f"/{self.slug}/delete"

    class Meta:
        db_table = 'blog_post'


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.subject

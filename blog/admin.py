from django.contrib import admin

# Register your models here.
from .models import BlogPost, Contact

admin.site.register(BlogPost)
admin.site.register(Contact)

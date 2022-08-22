from django.contrib import admin

# Register your models here.


from .models import SearchQuery

# admin.site.register(SearchQuery)
@admin.register(SearchQuery)
class SearchQueryAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ['id', 'user', 'query','timestamp']
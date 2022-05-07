from django.contrib import admin
from .models import *


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(BlogPostAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    list_display = ['title', 'author', 'published_date', 'last_updated', 'status']
    list_filter = ['author', 'published_date', 'last_updated', 'status']
    exclude = ['author']

from datetime import timezone
from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'published_at')
    list_filter = ('author', 'created_at', 'published_at')
    search_fields = ('title', 'content')

    def publish(self, request, queryset):
        queryset.update(published_at=timezone.now())

    actions = [publish]

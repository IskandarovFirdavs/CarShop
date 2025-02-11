from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'likes_count')
    search_fields = ('user__username', 'id')
    list_filter = ('user',)

    def likes_count(self, obj):
        return obj.likes.count()
    likes_count.short_description = 'Likes'


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user', 'approved')
    search_fields = ('user__username', 'post__id')
    list_filter = ('approved',)
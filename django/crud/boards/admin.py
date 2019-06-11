from django.contrib import admin
from .models import Board, Comment

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'contents', 'created_at', 'updated_at', ) # list_display: 약속된 변수명(조금 더 깔끔하게 나타내기 위한)

admin.site.register(Board, BoardAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'created_at', 'updated_at',)

admin.site.register(Comment, CommentAdmin)
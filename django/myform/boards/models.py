from django.db import models
from django.conf import settings

class Board(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_boards', blank=True) #blank=True: 좋아요를 누르지 않으면 빈 값을 넣어준다.

    def __str__(self):
        return f'글 번호 -> {self.id}, 글 제목 -> {self.title}, 글 내용 -> {self.content}'

class Comment(models.Model):
    content = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    class Meta:
        ordering = ('-pk',) # 최신 댓글이 위에 오도록
from django.db import models

class Board(models.Model): # Board class는 models.Model을 상속받는다
    title = models.CharField(max_length=10) # 최대 글자수 10 / TextField사용 --> 무제한
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True: 최초 그 값을 insert할 때 한번만 생성
    updated_at = models.DateTimeField(auto_now=True) # 게시글 수정시간 변경

    def __str__(self):
        return f'{self.id}번글 - {self.title} : {self.contents}'

class Comment(models.Model):
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE) # on_delete=models.CASCADE: 게시글 지워지면 달려있는 댓글 같이 지워지도록

    def __str__(self):
        return f'<Board{self.board_id}: Comment({self.id} - {self.content})>'
from django.db import models

class Board(models.Model): # Board class는 models.Model을 상속받는다
    title = models.CharField(max_length=10) # 최대 글자수 10 / TextField사용 --> 무제한
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # auto_now_add=True: 최초 그 값을 insert할 때 한번만 생성
    updated_at = models.DateTimeField(auto_now=True) # 게시글 수정시간 변경

    def __str__(self):
        return f'{self.id}번글 - {self.title} : {self.contents}'
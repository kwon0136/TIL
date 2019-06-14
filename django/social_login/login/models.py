from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    text = models.TextField()

# Create your models here.
def upload_file(instance, filename):
    #now=datetime.now()

    return f'files/{instance.from_user.pk}/{instance.id}_{filename}'

class Photo(models.Model):
    title = models.CharField(max_length=50, null=True)
    photo = models.FileField(upload_to=upload_file)
    message = models.TextField(null=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    print = models.BooleanField(null=True)

    def save(self, *args, **kwargs):
        if self.id is None:
            temp_image = self.photo
            self.photo = None
            super().save(*args, **kwargs)
            self.photo = temp_image
        super().save(*args, **kwargs)

    def __str__(self):
        return(f'{self.from_user.username}-{self.photo.name}-{self.print}')
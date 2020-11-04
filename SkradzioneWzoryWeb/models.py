from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField() #w przyszłości title i text do zmiany na plik
    created_date = models.DateTimeField(
        default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title

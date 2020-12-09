from django.db import models
from django.utils import timezone

class File(models.Model):
    name = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    equations = models.TextField()
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name

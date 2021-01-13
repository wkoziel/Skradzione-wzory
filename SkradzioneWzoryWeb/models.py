from typing import re

from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils import timezone

from .models import *

class File(models.Model):
    name = models.CharField(max_length=200, null=True)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name

    def list_all_files_from_database(self):
        files=[]
        all_files = File.objects.all()
        for file in all_files:
            files.append(file)
        return files




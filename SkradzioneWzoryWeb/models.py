from typing import re

from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils import timezone

"""Tworzenie migracji: python .\manage.py makemigrations SkradzioneWzoryWeb
    Wykonywanie migracji: python .\manage.py migrate """

class File(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    def list_all_files_from_database(self):
        files=[]
        all_files = File.objects.all()
        for file in all_files:
            files.append(file)
        return files

class Math(models.Model):
    math_text = models.CharField(max_length=200)
    hash_text = models.CharField(max_length=200)
    file_fk = models.ForeignKey(to=File, on_delete=models.CASCADE)

    def __str__(self):
        return self.math_text




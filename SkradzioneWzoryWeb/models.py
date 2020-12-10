from typing import re
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils import timezone
from .models import *
class File(models.Model):
    name = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    equations = models.TextField()
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.name
    def list_all_files_from_database(self):
        files=[]
        all_files = File.objects.all()
        for file in all_files:
            files.append(file)
        return files

    def _prepare_data(self, data):
        """Usuwa wszystkie znaki białe i zmienia tekst w jeden ciąg"""
        data = " ".join(data.split())
        data = data.replace(" ", "")
        self._separate_formulas(data)

    def _separate_formulas(self, data):
        """Wyszukuje wzory pomiędzy zadanymi komendami i zapisuje w liście jednowymiarowej math"""
        list = re.findall(r"\$\$(.+?)\$\$", data)
        self.math.extend(list)
        list = re.findall(r"\\\[(.+?)\\\]", data)
        self.math.extend(list)
        list = re.findall(r"\\\((.+?)\\\)", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{displaymath\}(.+?)\\end\{displaymath\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{math\}(.+?)\\end\{math\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{equation\}(.+?)\\end\{equation\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{equation\*\}(.+?)\\end\{equation\*\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{eqnarray\}(.+?)\\end\{eqnarray\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{eqnarray\*\}(.+?)\\end\{eqnarray\*\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{align\}(.+?)\\end\{align\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{align\*\}(.+?)\\end\{align\*\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{multline\}(.+?)\\end\{multline\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{multline\*\}(.+?)\\end\{multline\*\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{gather\}(.+?)\\end\{gather\}", data)
        self.math.extend(list)
        list = re.findall(r"\\begin\{gather\*\}(.+?)\\end\{gather\*\}", data)
        self.math.extend(list)
        list = re.findall(r"\$([^$]*)\$", data)
        list = [elem for elem in list if elem != ""]
        self.math.extend(list)

        self._print_stats(data)



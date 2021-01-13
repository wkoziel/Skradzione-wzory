import os
from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render
from SkradzioneWzoryWeb.models import File

from .alogrythm import *

def run_algorithms(request):
    if request.method == 'POST':
                    #user_file = File()
                    #context = user_file.list_all_files_from_database()
                    #print("Pliki dostepne w bazie danych to: ", context)
        uploaded_file = request.FILES['document']
        if uploaded_file.name.endswith(".tex"):
            context = alghoritm(uploaded_file.read().decode())
        else:
            context = "Nie udało się załadować pliku.\n Upewnij się że plik ma rozszerzenie .tex"
        return render(request, 'SkradzioneWzoryWeb/result.html', {'home': False, 'run': True, 'about': False, 'math': context})
    return render(request, 'SkradzioneWzoryWeb/run.html', {'home': False, 'run': True, 'about': False})


def about_project(request):
    return render(request, 'SkradzioneWzoryWeb/about.html', {'home': False, 'run': False, 'about': True})

def home_page(request):
    return render(request, 'SkradzioneWzoryWeb/welcome.html', {'home': True, 'run': False, 'about': False})
import os
from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render
from SkradzioneWzoryWeb.models import File

def run_algorithms (request):

    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        user_file = File()
        context = user_file.list_all_files_from_database()
        print("Pliki dostepne w bazie danych to: ", context)
        #drukuję w konsoli zawartość pobranego przez użytkownika pliku
        print(uploaded_file.read().decode())
        return render(request, 'SkradzioneWzoryWeb/run.html', {'instance': user_file, 'home': False, 'run': True, 'about': False})
    return render(request, 'SkradzioneWzoryWeb/run.html', {'home': False, 'run': True, 'about': False})

def about_project(request):
    return render(request, 'SkradzioneWzoryWeb/about.html', {'home': False, 'run': False, 'about': True})

def home_page(request):
    return render(request, 'SkradzioneWzoryWeb/welcome.html', {'home': True, 'run': False, 'about': False})
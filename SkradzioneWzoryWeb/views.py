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
        return render(request, 'SkradzioneWzoryWeb/run.html', {'instance': user_file})
    return render(request, 'SkradzioneWzoryWeb/run.html', {})

def about_project(request):
    return render(request, 'SkradzioneWzoryWeb/about.html', {})

def home_page(request):
    return render(request, 'SkradzioneWzoryWeb/welcome.html', {})
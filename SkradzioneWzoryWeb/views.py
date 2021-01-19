import os
from io import BytesIO

from django.http import HttpResponse
from django.shortcuts import render
from SkradzioneWzoryWeb.models import File, Math

from .alogrythm import *

def run_algorithms(request):
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['document']
            similarity = False

            if uploaded_file.name.endswith(".tex"):
                try:
                    context = alghoritm(uploaded_file.read().decode())
                    if len(context) == 0:
                        context = "Nie znaleziono podobnych plików w bazie danych."
                    else:
                        similarity = True
                except:
                    text = "W pliku znalazły się nieoczekiwane znaki."
                    return render(request, 'SkradzioneWzoryWeb/run.html', {'home': False, 'run': True, 'about': False, 'text': text})

            else:
                text = "Nie udało się załadować pliku.\n Upewnij się że plik ma rozszerzenie .tex"
                return render(request, 'SkradzioneWzoryWeb/run.html', {'home': False, 'run': True, 'about': False, 'text': text})

            return render(request, 'SkradzioneWzoryWeb/result.html', {'home': False, 'run': True, 'about': False, 'math': context, 'similarity': similarity})
        except:
            text = "Nie wybrano pliku."
            return render(request, 'SkradzioneWzoryWeb/run.html', {'home': False, 'run': True, 'about': False, 'text': text})

    return render(request, 'SkradzioneWzoryWeb/run.html', {'home': False, 'run': True, 'about': False})

def about_project(request):
    return render(request, 'SkradzioneWzoryWeb/about.html', {'home': False, 'run': False, 'about': True})

def home_page(request):
    return render(request, 'SkradzioneWzoryWeb/welcome.html', {'home': True, 'run': False, 'about': False})

def upload_page(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document'] #Tu zmień na swój form

        if uploaded_file.name.endswith(".tex"):

            """Dodawanie nazyw pliku"""
            file_name = uploaded_file.name
            upload_file = File.objects.create(name= file_name)
            upload_file.save()

            """Dodawanie wzorów do pliku"""
            file_to_read = uploaded_file.read().decode()
            math_from_file = get_file_math(file_to_read)
            hash_from_file = get_file_hash(file_to_read)

            for m, h in zip(math_from_file, hash_from_file):
                add_math = Math.objects.create(math_text = m, hash_text = str(h), file_fk = upload_file)
                add_math.save()

            return render(request, 'SkradzioneWzoryWeb/upload.html', {'text' : "Zakończono dodawanie pliku", 'colour': "rgb(49, 164, 43)"})
        else:
            return render(request, 'SkradzioneWzoryWeb/upload.html', {'text': "Coś poszło nie tak", 'colour': "rgb(194, 13, 13)"})
    return render(request, 'SkradzioneWzoryWeb/upload.html', {})
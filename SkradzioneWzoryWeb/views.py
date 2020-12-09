from django.http import HttpResponse
from django.shortcuts import render

def run_algorithms (request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request, 'SkradzioneWzoryWeb/run.html', {})

def about_project(request):
    return render(request, 'SkradzioneWzoryWeb/about.html', {})

def home_page(request):
    return render(request, 'SkradzioneWzoryWeb/welcome.html', {})
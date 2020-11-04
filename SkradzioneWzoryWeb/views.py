from django.shortcuts import render

def welcome_start(request):
    return render(request, 'SkradzioneWzoryWeb/welcome.html', {})
from django.shortcuts import render

def welcome_start(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print(uploaded_file.name)
        print(uploaded_file.size)
    return render(request, 'SkradzioneWzoryWeb/welcome.html', {})

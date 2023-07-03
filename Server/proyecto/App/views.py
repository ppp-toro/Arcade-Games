from django.shortcuts import render

def index(request):
    return render(request, 'general/template.html')

def registro(request):
    return render(request, 'registration/registro.html')

def login(request):
    return render(request, 'registration/login.html')


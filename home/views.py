from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def contato(request):
    return render(request, 'home/contato.html')

def login(request):
    return render(request, 'home/login.html')
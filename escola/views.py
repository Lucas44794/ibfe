from django.shortcuts import render, redirect
from django.contrib import auth, messages

def modulos(request):
    return render(request, 'escola/curso.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect("login")
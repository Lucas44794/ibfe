from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages

def modulos(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'escola/modulos.html')

def curso(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'escola/curso.html')

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect("login")
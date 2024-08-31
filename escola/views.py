from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from escola.models import Modulos, Cursos

def modulos(request):
    modulo = Modulos.objects.all()
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'escola/modulos.html', {"cards": modulo})

def curso(request):
    cursoModulos = Cursos.objects.all()
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'escola/dentroDoModulo.html', {"cards": cursoModulos})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect("login")
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from escola.models import Modulos, Cursos, Aluno

def modulos(request):
    modulo = Modulos.objects.all()
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'escola/modulos.html', {"cards": modulo})

def curso(request, curso_id):
    if not request.user.is_authenticated:
        return redirect('login')
    pega_curso = get_object_or_404(Modulos, pk=curso_id)
    cursoModulos = Cursos.objects.all()
    return render(request, 'escola/dentroDoModulo.html', {"cursoModulos": cursoModulos, "pega_curso": pega_curso})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect("login")
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth, messages
from escola.models import Modulos, Cursos, Aluno

def modulos(request):
    modulo = Modulos.objects.filter(publicado=True)
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'escola/modulos.html', {"cards": modulo})

def curso(request, curso_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    # Mapeamento de curso_id para nomes de módulos
    curso_nome = None
    if curso_id == 1:
        curso_nome = 'TEOLOGIA'
    elif curso_id == 2:
        curso_nome = 'PSICOLOGIA'
    elif curso_id == 3:
        curso_nome = 'HEBRAICO'
    
    # Filtrar cursos pelo nome do módulo
    cursoModulos = Cursos.objects.filter(modulo=curso_nome)
    
    return render(request, 'escola/dentroDoModulo.html', {"cursoModulos": cursoModulos})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso!")
    return redirect("login")
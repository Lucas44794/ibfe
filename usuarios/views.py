from django.shortcuts import render

from usuarios.forms import loginForms, CadastroForms

def login(request):
    form = loginForms()
    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForms()
    return render(request, 'usuarios/cadastro.html', {"form": form})

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from usuarios.forms import loginForms, CadastroForms
from django.contrib import auth

def login(request):
    form = loginForms()

    if request.method == 'POST':
        form = loginForms(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome_login']
            senha = form.cleaned_data['senha']

            usuario = auth.authenticate(
                request,
                username=nome,
                password=senha
            )
            if usuario is not None:
                auth.login(request, usuario)
                return redirect('index')
            else:
                return render(request, 'usuarios/login.html', {"form": form, "error": "Nome de usuário ou senha incorretos."})

    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form.cleaned_data['senha_1'] != form.cleaned_data['senha_2']:
                return render(request, 'usuarios/cadastro.html', {"form": form, "error": "As senhas não coincidem."})

            usuario = User.objects.create_user(
                username=form.cleaned_data['nome_cadastro'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['senha_1']
            )
            usuario.save()
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})

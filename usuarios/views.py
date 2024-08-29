from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from usuarios.forms import loginForms, CadastroForms
from django.contrib import auth, messages

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
                messages.success(request, f"{nome} logado com sucesso")
                return redirect('modulos')
            else:
                messages.error(request, "Erro ao efetuar o login")
                return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    form = CadastroForms()
    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form.cleaned_data['senha_1'] != form.cleaned_data['senha_2']:
                messages.error(request, "as senhas não são iguais")
                return render(request, 'usuarios/cadastro.html', {"form": form, "error": "As senhas não coincidem."})
            
            nome=form["nome_cadastro"].value()
            email = form["email"].value()
            senha = form["senha_1"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, "Usuario já cadastrado")
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome,
                email=form.email,
                password=senha
            )
            usuario.save()
            messages.success(request, "Cadastro efetuado com sucesso!")
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form": form})

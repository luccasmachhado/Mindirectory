from django.shortcuts import render
from.models import Curso
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

def home(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/home.html', {'cursos': cursos})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['password']
        user = authenticate(request, username=username, password=senha)
        if user is not None:
            auth_login(request, user)
            return redirect('/')  
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'cursos/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        senha = request.POST['password']
        confirmar = request.POST['confirm_password']

        if senha != confirmar:
            messages.error(request, 'As senhas não coincidem.')
            return redirect('cadastro')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Esse nome de usuário já está em uso.')
            return redirect('cadastro')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        messages.success(request, 'Conta criada com sucesso! Faça login.')
        return redirect('login')

    return render(request, 'cursos/cadastro.html')

def logout_view(request):
    auth_logout(request)
    return redirect('login')

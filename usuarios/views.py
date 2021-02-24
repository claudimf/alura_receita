from django.shortcuts import render, get_object_or_404


def cadastro(request):
    return render(request, 'usuarios/cadastro.html')


def login(request):
    return render(request, 'usuarios/login.html')


def dashboard(request):
    pass


def logout(request):
    pass

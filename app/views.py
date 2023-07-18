from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm

# Create your views here.

def index(request):
    return render(request, 'app/index.html')


def login(request):

    data = {
        'form': LoginForm()
    }

    if request.method == 'POST':
        formulario = LoginForm(data=request.POST)
        if formulario.is_valid():
            if verifyUser():
                formulario.save()
                data["mensaje"] = "llegamo pa"
                return redirect('nombreApp:index') #redireccionar a home
        else:
            data["form"] = formulario

    return render(request, 'app/login.html', data)

def verifyUser():
    return True

def register(request):

    data = {
        'form': RegisterForm()
    }

    if request.method == 'POST':
        formulario = RegisterForm(data=request.POST)
        if formulario.is_valid():
            if verifyUser():
                formulario.save()
                return redirect('nombreApp:index') #redireccionar a home
        else:
            data["form"] = formulario

    return render(request, 'app/register.html', data)
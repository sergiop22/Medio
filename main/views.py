from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .models import Perfil
from .forms import SignUpForm

# Create your views here.
def home(request):
    return render(request, 'layouts/home.html')

def index(request):
    return render(request, 'layouts/index.html')

def register(request):
    if request.method =="POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            usuario = authenticate(username=usuario, password=password)
            login(request, usuario)
            return redirect("index")
        else:
            print("Error")

    form = SignUpForm()
    return render(request, "auth/register.html", {"form": form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)

            if user is not None:
                login(request, user)
                return redirect("index")

            else:
                messages.error(request, "Usuario o contraseña equivocada")

    form = AuthenticationForm()
    return render(request, "auth/login.html", {"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "Saliste exitosamente")
    return redirect("home")
    
def user(request):
    return render(request, "user/user.html")

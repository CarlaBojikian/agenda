from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')


def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário ou senha inválido')
    return redirect('/')


@login_required(login_url='/login/')
def list_events(request):
    user = request.user
    evento = Evento.objects.filter(user_name=user)
    data = {'eventos':evento}
    return render(request, 'agenda.html', data)


def show_local(response, event_title):
    evento = Evento.objects.get(title=event_title)
    return HttpResponse('<h1>O evento será em {}</h1>'.format(evento.local))


def index(request):
    return redirect('/eventos-list/') # esta é uma maneira de fazer o redirecionamento

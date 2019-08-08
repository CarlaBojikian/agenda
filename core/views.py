from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404, JsonResponse


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
    actual_date = datetime.now() - timedelta(hours=1)  # timedelta vai subrtrair ou somar dias, horas ou minutos a data referida
    evento = Evento.objects.filter(user_name=user,
                                   date__gt=actual_date)  # __gt mostra os eventos atuais e __lt mostra os eventos passados
    data = {'eventos':evento}
    return render(request, 'agenda.html', data)


@login_required(login_url='/login/')
def new_event(request):
    evento_id = request.GET.get('id')
    dados = {}
    if evento_id:
        dados['evento'] = Evento.objects.get(id=evento_id)
    return render(request, 'events.html', dados)


@login_required(login_url='/login/')
def submit_event(request):
    if request.POST:
        title = request.POST.get('titulo')
        local = request.POST.get('local')
        description = request.POST.get('descricao')
        date = request.POST.get('data')
        user = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            Evento.objects.filter(id=id_evento).update(title=title,
                                                       local=local,
                                                       description=description,
                                                       date=date,
                                                       user_name=user)
        else:
            Evento.objects.create(title=title,
                                  local=local,
                                  description=description,
                                  date=date,
                                  user_name=user)
    return redirect('/')


@login_required(login_url='/login/')
def delete_event(request, evento_id):
    usuario = request.user
    try:
        evento = Evento.objects.get(id=evento_id)
    except Exception:
        raise Http404
    if usuario == evento.user_name:
        evento.delete()
    else:
        raise Http404()
    return redirect('/')


def show_local(response, event_title):
    evento = Evento.objects.get(title=event_title)
    return HttpResponse('<h1>O evento será em {}</h1>'.format(evento.local))


def index(request):
    return redirect('/eventos-list/') # esta é uma maneira de fazer o redirecionamento


@login_required(login_url='/login/')
def json_list(request):
    user = request.user
    evento = Evento.objects.filter(user_name=user).values('id','title')
    return JsonResponse(list(evento), safe=False)

from django.shortcuts import render, HttpResponse, redirect
from core.models import Evento


# Create your views here.


def show_local(response, event_title):
    evento = Evento.objects.get(title=event_title)
    return HttpResponse('<h1>O evento será em {}</h1>'.format(evento.local))


def list_events(request):
    user = request.user
    evento = Evento.objects.filter(user_name=user)
    data = {'eventos':evento}
    return render(request, 'agenda.html', data)


def index(request):
    return redirect('/eventos-list/') # esta é uma maneira de fazer o redirecionamento

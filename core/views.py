from django.shortcuts import render, HttpResponse
from core.models import Evento


# Create your views here.

def gerar_pessoa(cor_do_cabelo="preto", cor_dos_olhos="verde", tamanho_do_pe=None, cor_da_pele=None):
    print()
    pass


def show_local(response, event_title):
    evento = Evento.objects.get(title=event_title)
    answer = '<h1>O evento será em {}</h1>'.format(evento.local)
    return HttpResponse(answer)

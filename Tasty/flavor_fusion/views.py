from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    return render (request, 'login.html')

def cadastro(request):
    return HttpResponse(request, 'flavor_fusion/templates/cadastro.html')

def filtrarreceita(request):
    return HttpResponse(request, 'flavor_fusion/templates/filtrarreceita.html')

def novareceita(request):
    return HttpResponse(request, 'flavor_fusion/templates/novareceita.html')

def historico(request):
    return HttpResponse(request, 'flavor_fusion/templates/historico.html')




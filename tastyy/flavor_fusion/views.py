from django.shortcuts import render

def login(request):
    return render(request, 'flavor_fusion/login.html')

def cadastro(request):
    return render(request, 'flavor_fusion/cadastro.html')

def filtrarreceita(request):
    return render(request, 'flavor_fusion/filtrarreceita.html')

def novareceita(request):
    return render(request, 'flavor_fusion/novarreceita.html')
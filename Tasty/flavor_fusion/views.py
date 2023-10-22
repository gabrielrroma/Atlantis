from django.shortcuts import render


def login(request):
    return render(request, 'flavor_fusion/login.html')




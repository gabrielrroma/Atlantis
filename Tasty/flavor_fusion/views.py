from django.shortcuts import render

def index(request):
    return render(request, 'flavor_fusion/index.html')



from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context)

def about(request):
    context = {}
    return render(request, 'rango/about.html', context=context)

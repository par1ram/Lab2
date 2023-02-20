from django.shortcuts import render
from django.http import HttpResponse


"""def home(request):
    return HttpResponse('Привет мир!')"""


def home(request):
    return render(request, 'index.html')


def mystyles(request):
    return render(request, 'static_handler.html')



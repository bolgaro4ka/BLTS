from django.shortcuts import render, redirect
from django.conf import settings
# Create your views here.
def index(request):

    return render(request, 'index.html', {'v': settings.VERSION})

def cat_error(request, cat):
    error={}
    error["name"] = f"Критическая ошибка ({cat})"
    error["message"] = "Detected cats!"
    error["img"] = f'https://http.cat/{cat}'
    return render(request, 'errors.html', {'error': error})
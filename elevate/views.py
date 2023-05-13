from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Prueba correcta en EC2 Por cierto Jason es HACKER</h1>')
from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse('esto es el login ')

def Register(request):
    return HttpResponse('esto es el registro ')

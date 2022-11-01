from http.client import HTTPResponse
from django.shortcuts import render, redirect

# Create your views here.

def Home(request):
    context = {'mensagem': 'Ola Mundo'}
    return render(request, 'core/index.html', context=context)
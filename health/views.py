from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ping(request):
    print(f"client's request {request}")
    return HttpResponse('pong')
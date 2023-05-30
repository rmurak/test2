from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def january (request):
    return HttpResponse("January challenge")
def february (request):
    return HttpResponse("February challenge")
def march (request):
    return HttpResponse("March challenge")


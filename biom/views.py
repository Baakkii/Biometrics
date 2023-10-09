from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requset):
    return  HttpResponse("Hello, world. You'r at the thise web app")

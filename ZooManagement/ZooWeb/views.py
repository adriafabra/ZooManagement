from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main_url(req):
    return HttpResponse("Welcome to Zoo Management")

def zooweb_url(req):
    return HttpResponse("Here you can manage the zoo")
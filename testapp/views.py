from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hii This is shivam")

def home(request):
    return HttpResponse("Hii This is home page")

def about(request):
    return HttpResponse("Hii This is about page")


def main(request):
    return HttpResponse("Hii This is the main page")

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hii This is shivam")

def home(request):
    res= render(request,'testapp/home.html')
    return res

def about(request):
    return HttpResponse("Hii This is about page")


def main(request):
    return HttpResponse("Hii This is the main page")

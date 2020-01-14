from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hii This is shivam")

def home(request):
    que="This is zinza format"
    level="1234567890"
    data={'que':que, 'level':level}
    return render(request,'testapp/home.html', context=data)


def about(request):
    msg="this is best message"
    return render(request,'testapp/about.html',{'msg':msg})


def main(request):
    return HttpResponse("Hii This is the main page")

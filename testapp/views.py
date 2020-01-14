from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import Employee

# Create your views here.

def index(request):
    return HttpResponse("Hii This is shivam")

def employee_info_view(request):
    employees=Employee.objects.all()
    data={'employees':employees}
    return render(request,'testapp/employees.html',data)

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

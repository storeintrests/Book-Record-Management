from django.shortcuts import render
from BRMapp.forms import NewBookForm
from BRMapp.models import Book
from django.http import HttpResponse

# Create your views here.

def viewBooks(request):
    books = Book.objects.all()
    res=render(request,'BRMapp/view_book.html',{'books':books})
    return res


def newBook(request):
    form = NewBookForm()
    res = render(request,'BRMapp/new_book.html',{'form':form})
    return res

def add(request):
    if request.method == "POST":
        form = NewBookForm(request.POST)
        book = Book()
        book.title= form.data['title']
        book.price = form.data['price']
        book.author = form.data['author']
        book.publisher = form.data['publisher']
        book.save()
    s="Record Stored <br> <a href='/BRMapp/view-books'> View All Books</a>"
    return HttpResponse(s)

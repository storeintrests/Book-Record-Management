from django.contrib import admin
from django.urls import path
from BRMapp import views

urlpatterns = [
    path('newbook/',views.newBook),
    path('add',views.add),
    path('view-books',views.viewBooks),
    path('edit-book',views.editBook),
    path('edit',views.edit),
    path('delete-book', views.deleteBook),
    path('search-book', views.searchBook),
    path('search',views.search),
    path('login',views.userLogin),
    path('logout',views.userLogout),
    path('',views.index),
]

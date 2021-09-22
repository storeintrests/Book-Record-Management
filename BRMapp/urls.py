from django.contrib import admin
from django.urls import path
from BRMapp import views

# urlpatterns = [
#     path('newbook/', views.newBook),
#     path('add', views.add),
#     path('view-books', views.viewBooks),
#     path('edit-book', views.editBook),
#     path('edit', views.edit),
#     path('delete-book', views.deleteBook),
#     path('search-book', views.searchBook),
#     path('search', views.search),
#     path('login', views.userLogin),
#     path('logout', views.userLogout),
#     path('', views.index),
# ]

urlpatterns = [
    path('/', views.view_apply),
    path('', views.view_apply),
    path('history/', views.view_history),
    path('passed/', views.view_passed),
    path('rejected/', views.view_rejected),
    path('api/passed', views.pass_apply),
    path('api/reject', views.reject_apply),
]

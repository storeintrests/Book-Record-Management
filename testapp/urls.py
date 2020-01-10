from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('',views.index),
    path('home',views.home),
    path('main',views.main),
    path('about',views.about),
    #path('admin/', admin.site.urls),
]

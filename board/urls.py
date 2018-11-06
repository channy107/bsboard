from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home', home),
    path('login', login, name='login'),
    path('join', join, name='join'),
    path('id_check', id_check, name='id_check'),
    path('board1', board1, name='board1'),
    path('writePage', writePage, name='writePage'),
    path('detail', detail, name='detail'),
    path('afterlogin', afterlogin, name='afterlogin'),

]

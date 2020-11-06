from django.contrib import admin
from django.urls import path, include
from simplemooc.courses.views import index

urlpatterns = [
    path('', index, name='index'),
]
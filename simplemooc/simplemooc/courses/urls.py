from django.contrib import admin
from django.urls import path, include
from simplemooc.courses.views import index, details

urlpatterns = [
    path('', index, name='index'),
    path('/details/<slug:slug>/', details, name='details'),
    # path(r'^(?P<key>\d+)/$', details, name='details'),
]
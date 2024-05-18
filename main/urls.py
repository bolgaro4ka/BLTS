from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
    path('', views.index),
    path('t/', include('tests.urls')),
    path('a/', include('account.urls')),
    path('s/', include('session.urls')),
    path('e/<int:cat>', views.cat_error),    
]

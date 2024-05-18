from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
    path('', views.listOfTests),
    path('raw', views.test_view_iframe),
    path('<int:id_test>/', views.test_view),
    path('<int:id_test>/end', views.end_view),
]

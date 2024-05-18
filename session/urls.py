from django.contrib import admin
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
    path('', views.index),
    path('<int:id>', views.session),
    path('leaderboard/<int:id>', views.leaderboard),
    path('leaderboard/api/<int:id>', views.leaderboard_api),

]

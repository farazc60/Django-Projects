from django.urls import path
from . import views

urlpatterns = [
    path('', views.count_words, name='count_words'),
]
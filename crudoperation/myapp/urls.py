from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('book/create/', views.create_book, name='create_book'),
    path('book/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('book/<int:book_id>/delete/', views.delete_book, name='delete_book'),
]
from django.urls import path
from user_media import views

urlpatterns = [
    path('books/', views.book_view, name='book_view'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
]

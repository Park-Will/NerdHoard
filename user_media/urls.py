from django.urls import path
from user_media import views

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('add_book/', views.add_book, name='add_book'),
    path('search_book/', views.search_book, name='search_book'),
    path('edit_book/<int:book_id>/<int:page_number>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/<int:page_number>/', views.delete_book, name='delete_book'),
]

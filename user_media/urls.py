from django.urls import path
from user_media import views

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('add_book/', views.add_book, name='add_book'),
    path('search_book/', views.search_book, name='search_book'),
    path('edit_book/<int:book_id>/<int:page_number>/', views.edit_book, name='edit_book'),
    path('edit_book_full/<int:book_id>/<int:page_number>/', views.edit_book_full, name='edit_book_full'),
    path('delete_book/<int:book_id>/<int:page_number>/', views.delete_book, name='delete_book'),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('search_movie/', views.search_movie, name='search_movie'),
    path('edit_movie/<int:movie_id>/<int:page_number>/', views.edit_movie, name='edit_movie'),
    path('delete_movie/<int:movie_id>/<int:page_number>/', views.delete_movie, name='delete_movie'),
    path('add_tv/', views.add_tv, name='add_tv'),
    path('search_tv/', views.search_tv, name='search_tv'),
    path('edit_tv/<int:tv_id>/<int:page_number>/', views.edit_tv, name='edit_tv'),
    path('delete_tv/<int:tv_id>/<int:page_number>/', views.delete_tv, name='delete_tv'),
    path('add_videogame/', views.add_videogame, name='add_videogame'),
    path('search_videogame/', views.search_videogame, name='search_videogame'),
    path('edit_videogame/<int:videogame_id>/<int:page_number>/', views.edit_videogame, name='edit_videogame'),
    path('delete_videogame/<int:videogame_id>/<int:page_number>/', views.delete_videogame, name='delete_videogame'),
]

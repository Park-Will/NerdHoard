from django.urls import path
from user_media import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
    path('books/', views.book_view, name='book_view'),
    path('books/edit/<int:book_id>/', views.edit_book, name='edit_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),
    path('movies/', views.movie_view, name='movie_view'),
    path('movies/edit/<int:movie_id>/', views.edit_movie, name='edit_movie'),
    path('movies/delete/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('tv/', views.tv_view, name='tv_view'),
    path('tv/edit/<int:tv_id>/', views.edit_tv, name='edit_tv'),
    path('tv/delete/<int:tv_id>/', views.delete_tv, name='delete_tv'),
    path('videogames/', views.videogame_view, name='videogame_view'),
    path('videogames/edit/<int:videogame_id>/', views.edit_videogame, name='edit_videogame'),
    path('videogames/delete/<int:videogame_id>/', views.delete_videogame, name='delete_videogame')
]

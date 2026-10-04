from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Movie, TV, VideoGame
from .forms import BookForm, MovieForm, TVForm, VideoGameForm
from django.core.paginator import Paginator
import requests
from .openlibraryAPI import *
from .tmdbAPI import *

#TODO: Build tv, and videogame API files; wire them into the add_<object> functions here and update their individual css.html templates
#TODO: Wire updated 'full edit' views to templates (Movie, TV, VideoGame)

def hello_world(request):
	return HttpResponse('Hello, World!<br><br>This is the root page of NerdHoard!')

def front_page(request):
        return render(request, 'index_css.html')

def add_book(request):
        success = False
        added_book = None
        if request.method == "POST":
                form = BookForm(request.POST)
                if form.is_valid():
                        new_book = form.save()
                        success = True
                        added_book = new_book
                        return render( request, "add_book_css.html",
                        {"form": form,
                        "added_book": added_book,
                        "success": success},
                        )
        else:
                summary = ''
                openlibrary_key = request.GET.get('openlibrary_key', '')
                if openlibrary_key.startswith('/works/'):
                        try:
                                summary = book_summary(openlibrary_key)
                        except requests.exceptions.RequestException:
                                summary = ''

                form = BookForm(initial={
                        'title': request.GET.get('title', ''),
                        'author': request.GET.get('author', ''),
                        'cover_url': request.GET.get('cover_url', ''),
                        'release_year': request.GET.get('year', ''),
                        'summary': summary,

                })

        user_query = request.GET.get('search', '').strip()
        results = []
        if user_query:
                try:
                        results = book_search(user_query)
                except requests.exceptions.RequestException:
                        results = []

        return render(request, 'add_book_css.html',
                        {'form': form,
                        'added_book': added_book,
                        'success': success,
                        'user_query': user_query,
                        'results': results,
                        })

def search_book(request):
        page_number = request.GET.get('page', 1)
        title = request.GET.get('title', '').strip()
        author = request.GET.get('author', '').strip()
        series = request.GET.get('series', '').strip()

        if request.method == 'POST':
                title = request.POST.get('title', '').strip()
                author = request.POST.get('author', '').strip()
                series = request.POST.get('series', '').strip()
                page_number = 1

        if title or author or series:
                books = Book.objects.filter(title__icontains=title, author__icontains=author, series__icontains=series).order_by('id')
        else:
                books = Book.objects.all().order_by('id')

        paginator = Paginator(books, 10)
        page_obj = paginator.get_page(page_number)

        return render(request, 'search_book_css.html',{
                'books': page_obj,
                'title_query': title,
                'author_query': author,
                'series_query': series
        })

def edit_book(request, book_id, page_number):
        pn = request.GET.get('page', page_number)
        print(f'[DBG] edit_book {book_id}, {page_number}, {pn} <<<')
        success = False

        book_list = Book.objects.all().order_by('id')
        paginator = Paginator(book_list, 10)
        page_number = request.POST.get('page', request.GET.get('page', page_number))
        page_obj = paginator.get_page(page_number)
        return render(request, 'edit_book_css.html',{
                'books': page_obj,
                'success': success,
                'updated_book_id': book_id,
        })

def edit_book_full(request, book_id, page_number):
        book = get_object_or_404(Book, id=book_id)

        if request.method == 'POST':
                form = BookForm(request.POST, instance=book)
                if form.is_valid():
                        form.save()
                        return redirect('edit_book', book_id=book_id, page_number=page_number)
        else:
                form = BookForm(instance=book)

        return render(request, 'edit_book_full_css.html', {
                'form': form,
                'book': book,
                'page_number': page_number
        })
                
def delete_book(request, book_id, page_number):
        print("[DBG] delete_book called for ID:", book_id)
        if request.method == "POST":
                book = get_object_or_404(Book, id=book_id)
                book.delete()
        # Redirect to the same page number after delete
        return redirect("edit_book", book_id=book_id, page_number=page_number)

def add_movie(request):
        success = False
        added_movie = None
        if request.method == "POST":
                form = MovieForm(request.POST)
                if form.is_valid():
                        new_movie = form.save()
                        success = True
                        added_movie = new_movie
                        return render( request, "add_movie_css.html",{
                                "form": form,
                                "added_movie": added_movie,
                                "success": success
                                })
        else:
                director = ''
                tmdb_id = request.GET.get('tmdb_id', '')
                if tmdb_id.isdigit():
                        try:
                                director = movie_details(tmdb_id)['director']
                        except requests.exceptions.RequestException:
                                director = ''

                form = MovieForm(initial={
                        'title': request.GET.get('title', ''),
                        'cover_url': request.GET.get('cover_url', ''),
                        'release_year': request.GET.get('release_date', '')[:4] or None,
                        'summary': request.GET.get('summary', ''),
                        'director': director,
                        })

        user_query = request.GET.get('search', '').strip()
        results = []
        if user_query:
                try:
                        results = movie_search(user_query)
                except requests.exceptions.RequestException:
                        results = []

        return render(request, "add_movie_css.html", {
                "form": form,
                "added_movie": added_movie,
                "success": success,
                'user_query': user_query,
                'results': results,
                })

def search_movie(request):
        page_number = request.GET.get('page', 1)
        title = request.GET.get('title', '').strip()
        director = request.GET.get('director', '').strip()
        series = request.GET.get('series', '').strip()

        if request.method == 'POST':
                title = request.POST.get('title', '').strip()
                director = request.POST.get('director', '').strip()
                series = request.POST.get('series', '').strip()
                page_number = 1

        if title or director or series:
                movies = Movie.objects.filter(title__icontains=title, director__icontains=director, series__icontains=series).order_by('id')
        else:
                movies = Movie.objects.all().order_by('id')

        paginator = Paginator(movies, 10)
        page_obj = paginator.get_page(page_number)

        return render(request, 'search_movie_css.html',{
                'movies': page_obj,
                'title_query': title,
                'director_query': director,
                'series_query': series
        })

def edit_movie(request, movie_id, page_number):
        pn = request.GET.get('page', page_number)
        print(f'[DBG] edit_movie {movie_id}, {page_number}, {pn} <<<')
        success = False

        movie_list = Movie.objects.all().order_by('id')
        paginator = Paginator(movie_list, 10)
        page_number = request.POST.get('page', request.GET.get('page', page_number))
        page_obj = paginator.get_page(page_number)
        return render(request, 'edit_movie_css.html',{
                'movies': page_obj,
                'success': success,
                'updated_movie_id': movie_id,
        })

def edit_movie_full(request, movie_id, page_number):
        movie = get_object_or_404(Movie, id=movie_id)

        if request.method == 'POST':
                form = MovieForm(request.POST, instance=movie)
                if form.is_valid():
                        form.save()
                        return redirect('edit_movie', movie_id = movie_id, page_number = page_number)
        else:
                form = MovieForm(instance = movie)

        return render(request, 'edit_movie_full_css.html', {
                'form': form,
                'movie': movie,
                'page_number': page_number
        })

def delete_movie(request, movie_id, page_number):
        print("[DBG] delete_movie called for ID:", movie_id)
        if request.method == "POST":
                movie = get_object_or_404(Movie, id=movie_id)
                movie.delete()
                # Redirect to the same page number after delete
                return redirect("edit_movie", movie_id=movie_id, page_number=page_number)
        
        return redirect("edit_movie", movie_id=movie_id, page_number=page_number)

def add_tv(request):
        success = False
        added_tv = None
        if request.method == "POST":
                form = TVForm(request.POST)
                if form.is_valid():
                        new_tv = form.save()
                        success = True
                        added_tv = new_tv
                        return render( request, "add_tv_css.html",{
                                "form": form,
                                "added_tv": added_tv,
                                "success": success
                                })      
        else:
                form = TVForm()
        return render(request, "add_tv_css.html",{
                "form": form,
                "added_tv": added_tv,
                "success": success
                })

def search_tv(request):
        page_number = request.GET.get('page', 1)
        title = request.GET.get('title', '').strip()
        creator = request.GET.get('creator', '').strip()

        if request.method == 'POST':
                title = request.POST.get('title', '').strip()
                creator = request.POST.get('creator', '').strip()
                page_number = 1

        if title or creator:
                tvs = TV.objects.filter(title__icontains=title, creator__icontains=creator).order_by('id')
        else:
                tvs = TV.objects.all().order_by('id')

        paginator = Paginator(tvs, 10)
        page_obj = paginator.get_page(page_number)

        return render(request, 'search_tv_css.html',{
                'tvs': page_obj,
                'title_query': title,
                'creator_query': creator,
        })

def edit_tv(request, tv_id, page_number):
        pn = request.GET.get('page', page_number)
        print(f'[DBG] edit_tv {tv_id}, {page_number}, {pn} <<<')
        success = False


        tv_list = TV.objects.all().order_by('id')
        paginator = Paginator(tv_list, 10)
        page_number = request.POST.get('page', request.GET.get('page', page_number))
        page_obj = paginator.get_page(page_number)
        return render(request, 'edit_tv_css.html',{
                'tvs': page_obj,
                'success': success,
                'updated_tv_id': tv_id,
        })


def edit_tv_full(request, tv_id, page_number):
        tv = get_object_or_404(TV, id=tv_id)

        if request.method == 'POST':
                form = TVForm(request.POST, instance=tv)
                if form.is_valid():
                        form.save()
                        return redirect('edit_tv', tv_id = tv_id, page_number = page_number)
        else:
                form = TVForm(instance = tv)

        return render(request, 'edit_tv_full_css.html', {
                'form': form,
                'tv': tv,
                'page_number': page_number
        })

def delete_tv(request, tv_id, page_number):
        print("[DBG] delete_tv called for ID:", tv_id)
        if request.method == "POST":
                tv = get_object_or_404(TV, id=tv_id)
                tv.delete()
                # Redirect to the same page number after delete
                return redirect("edit_tv", tv_id=tv_id, page_number=page_number)

        return redirect("edit_tv", tv_id=tv_id, page_number=page_number)

def add_videogame(request):
        success = False
        added_videogame = None
        if request.method == "POST":
                form = VideoGameForm(request.POST)
                if form.is_valid():
                        new_videogame = form.save()
                        success = True
                        added_videogame = new_videogame
                        return render( request, "add_videogame_css.html",{
                                "form": form,
                                "added_videogame": added_videogame,
                                "success": success
                                })      
        else:
                form = VideoGameForm()
        return render(request, "add_videogame_css.html",{
                "form": form,
                "added_videogame": added_videogame,
                "success": success
                })

def search_videogame(request):
        page_number = request.GET.get('page', 1)
        title = request.GET.get('title', '').strip()
        developer = request.GET.get('developer', '').strip()
        series = request.GET.get('series', '').strip()


        if request.method == 'POST':
                title = request.POST.get('title', '').strip()
                developer = request.POST.get('developer', '').strip()
                series = request.POST.get('series', '').strip()
                page_number = 1

        if title or developer or series:
                videogames = VideoGame.objects.filter(title__icontains=title, developer__icontains=developer, series__icontains=series).order_by('id')
        else:
                videogames = VideoGame.objects.all().order_by('id')

        paginator = Paginator(videogames, 10)
        page_obj = paginator.get_page(page_number)

        return render(request, 'search_videogame_css.html',{
                'videogames': page_obj,
                'title_query': title,
                'developer_query': developer,
                'series_query': series
        })

def edit_videogame(request, videogame_id, page_number):
        pn = request.GET.get('page', page_number)
        print(f'[DBG] edit_videogame {videogame_id}, {page_number}, {pn} <<<')
        success = False

        videogame_list = VideoGame.objects.all().order_by('id')
        paginator = Paginator(videogame_list, 10)
        page_number = request.POST.get('page', request.GET.get('page', page_number))
        page_obj = paginator.get_page(page_number)
        return render(request, 'edit_videogame_css.html',{
                'videogames': page_obj,
                'success': success,
                'updated_videogame_id': videogame_id,
        })

def edit_videogame_full(request, videogame_id, page_number):
        videogame = get_object_or_404(VideoGame, id=videogame_id)

        if request.method == 'POST':
                form = VideoGameForm(request.POST, instance = videogame)
                if form.is_valid():
                        form.save()
                        return redirect('edit_videogame', videogame_id = videogame_id, page_number = page_number)
        else:
                form = VideoGameForm(instance = videogame)

        return render(request, 'edit_videogame_full_css.html', {
                'form': form,
                'videogame': videogame,
                'page_number': page_number
        })

def delete_videogame(request, videogame_id, page_number):
        print("[DBG] delete_videogame called for ID:", videogame_id)
        if request.method == "POST":
                videogame = get_object_or_404(VideoGame, id=videogame_id)
                videogame.delete()
                # Redirect to the same page number after delete
                return redirect("edit_videogame", videogame_id=videogame_id, page_number=page_number)

        return redirect("edit_videogame", videogame_id=videogame_id, page_number=page_number)
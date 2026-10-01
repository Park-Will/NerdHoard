from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Movie, TV, VideoGame
from .forms import BookForm, MovieForm, TVForm, VideoGameForm
from django.core.paginator import Paginator

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
        form = BookForm()
    return render(request, "add_book_css.html",
        {"form": form,
         "added_book": added_book,
         "success": success},
    )

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

        if request.method == 'POST':
                book = Book.objects.get(id=book_id)
                title = request.POST.get('title')
                author = request.POST.get('author')
                publisher = request.POST.get('publisher')
                release_date = request.POST.get('release_date')
                isbn = request.POST.get('isbn')
                series = request.POST.get('series')
                series_num = request.POST.get('series_num')
                cover_url = request.POST.get('cover_url')
                summary = request.POST.get('summary')
                notes = request.POST.get('notes')
                condition = request.POST.get('condition')
                form = BookForm(request.POST, instance=book)
                
                if book.title != title or book.author != author or book.publisher != publisher or book.release_date != release_date or book.isbn != isbn or book.series != series or book.series_num != series_num or book.cover_url != cover_url or book.summary != summary or book.notes != notes or book.condition != condition:
                        book.title = title
                        book.author = author
                        book.publisher = publisher
                        book.release_date = release_date
                        book.isbn = isbn
                        book.series = series
                        book.series_num = series_num
                        book.cover_url = cover_url
                        book.summary = summary
                        book.notes = notes
                        book.condition = condition
                        book.save()
                        success = True

        book_list = Book.objects.all()
        paginator = Paginator(book_list, 10)
        page_number = request.POST.get('page', request.GET.get('page', page_number))
        page_obj = paginator.get_page(page_number)
        return render(request, 'edit_book_css.html',{
                'books': page_obj,
                'success': success,
                'updated_book_id': book_id,
        })

def delete_book(request, book_id):
	book = get_object_or_404(Book, id=book_id)
	book.delete()
	return redirect('book_view')

def movie_view(request):
        movies = Movie.objects.all()

        if request.method == 'POST':
                form = MovieForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('movie_view')
        else:
                form = MovieForm()

        return render(request, 'movie_list.html', {'form': form, 'movies': movies})

def edit_movie(request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)

        if request.method == 'POST':
                form = MovieForm(request.POST, instance=movie)
                if form.is_valid():
                        form.save()
                        return redirect('movie_view')
        else:
                form = MovieForm(instance=movie)

        return render(request, 'movie_edit.html', {'form': form, 'movie': movie})

def delete_movie(request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        movie.delete()
        return redirect('movie_view')

def tv_view(request):
        tvs = TV.objects.all()

        if request.method == 'POST':
                form = TVForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('book_view')
        else:
                form = TVForm()

        return render(request, 'tv_list.html', {'form': form, 'tvs': tvs})

def edit_tv(request, tv_id):
        tv = get_object_or_404(TV, id=tv_id)

        if request.method == 'POST':
                form = TVForm(request.POST, instance=tv)
                if form.is_valid():
                        form.save()
                        return redirect('tv_view')
        else:
                form = TVForm(instance=tv)

        return render(request, 'tv_edit.html', {'form': form, 'tv': tv})

def delete_tv(request, tv_id):
        tv = get_object_or_404(TV, id=tv_id)
        tv.delete()
        return redirect('tv_view')

def videogame_view(request):
        videogames = VideoGame.objects.all()

        if request.method == 'POST':
                form = VidoeoGameForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('book_view')
        else:
                form = VideoGameForm()

        return render(request, 'videogame_list.html', {'form': form, 'videogames': videogames})

def edit_videogame(request, videogame_id):
        videogame = get_object_or_404(VideoGame, id=videogame_id)

        if request.method == 'POST':
                form = VideoGameForm(request.POST, instance=videogame)
                if form.is_valid():
                        form.save()
                        return redirect('videogame_view')
        else:
                form = VideoGameForm(instance=videogame)

        return render(request, 'videogame_edit.html', {'form': form, 'videogame': videogame})

def delete_videogame(request, videogame_id):
        videogame = get_object_or_404(VideoGame, id=videogame_id)
        videogame.delete()
        return redirect('videogame_view')

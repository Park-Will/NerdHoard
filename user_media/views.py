from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book, Movie, TV, VideoGame
from .forms import BookForm, MovieForm, TVForm, VideoGameForm

def hello_world(request):
	return HttpResponse('Hello, World!<br><br>This is the root page of NerdHoard!')

def book_view(request):
	books = Book.objects.all()

	if request.method == 'POST':
		form = BookForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('book_view')
	else:
		form = BookForm()

	return render(request, 'book_list.html', {'form': form, 'books': books})

def edit_book(request, book_id):
	book = get_object_or_404(Book, id=book_id)

	if request.method == 'POST':
		form = BookForm(request.POST, instance=book)
		if form.is_valid():
			form.save()
			return redirect('book_view')
	else:
		form = BookForm(instance=book)

	return render(request, 'book_edit.html', {'form': form, 'book': book})

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

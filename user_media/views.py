from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

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

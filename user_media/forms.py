from django import forms
from .models import Book, Movie, TV, VideoGame

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title', 'author', 'publisher', 'release_date', 'isbn', 'series', 'series_num', 'cover_url', 'summary', 'notes', 'condition']

class MovieForm(forms.ModelForm):
	class Meta:
		model = Movie
		fields = ['title', 'director', 'release_date', 'format', 'series', 'series_num', 'cover_url', 'summary', 'notes', 'condition']

class TVForm(forms.ModelForm):
	class Meta:
		model = TV
		fields = ['title', 'creator', 'release_date', 'format', 'season', 'cover_url', 'summary', 'notes', 'condition']

class VideoGameForm(forms.ModelForm):
	class Meta:
		model = VideoGame
		fields = ['title', 'developer', 'publisher', 'release_date', 'platform', 'series', 'series_num', 'cover_url', 'summary', 'notes', 'condition']

from django import forms
from .models import Book, Movie, TV, VideoGame

class BookForm(forms.ModelForm):
	class Meta:
		model = Book
		fields = ['title', 'author', 'publisher', 'release_date', 'isbn', 'series', 'series_num', 'cover_url', 'summary', 'notes', 'condition']
		widgets = {
			'title': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Book Title',
			}),
			'author': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Author'
			}),
			'publisher': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Publisher'
			}),
			'release_date': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Publication Date'
			}),
			'isbn': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter ISBN'
			}),
			'series': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Series'
			}),
			'series_num': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter number in Series'
			}),
			'cover_url': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter URL to Cover Image'
			}),
			'summary': forms.Textarea(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Summary'
			}),
			'notes': forms.Textarea(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Notes'
			}),
			'condition': forms.Select(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Condition of your copy'
			})
		}
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

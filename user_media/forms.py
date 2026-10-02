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
		widgets = {
			'title': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Book Title',
			}),
			'director': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Director'
			}),
			'format': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Format'
			}),
			'release_date': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Release Date'
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
class TVForm(forms.ModelForm):
	class Meta:
		model = TV
		fields = ['title', 'creator', 'release_date', 'format', 'season', 'cover_url', 'summary', 'notes', 'condition']
		widgets = {
			'title': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Book Title',
			}),
			'creator': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Creator'
			}),
			'release_date': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Release Date'
			}),
			'format': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter format'
			}),
			'season': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Season'
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
class VideoGameForm(forms.ModelForm):
	class Meta:
		model = VideoGame
		fields = ['title', 'developer', 'publisher', 'release_date', 'platform', 'series', 'series_num', 'cover_url', 'summary', 'notes', 'condition']
		widgets = {
			'title': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Book Title',
			}),
			'developer': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Developer'
			}),
			'publisher': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Publisher'
			}),
			'release_date': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Release Date'
			}),
			'platform': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Enter Platform'
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
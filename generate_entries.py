import os
import django

# Ensure Django settings are properly loaded
# Update 'djangoproject' with project name
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NerdHoard.settings')
# This must be called before importing models
django.setup()

from user_media.models import Book, Movie, TV, VideoGame
from faker import Faker

fake = Faker()

def generate_books(count=100):
	"""
	Generates and inserts 'count' number of books into the database.
	"""
	try:
		sample_books = [Book(
			title = ' '.join(fake.words(4)),
			author = fake.name(),
			publisher = ' '.join(fake.words(2)),
			release_year = fake.year(),
			isbn = fake.numerify(text="#############"),
			series = ' '.join(fake.words(4)),
			series_num = fake.random_int(min=1, max=12),
			summary = fake.paragraph(),
			notes = fake.paragraph(),
			condition = 'Good'
		)
		for i in range(count)
		]

		Book.objects.bulk_create(sample_books)

		print(f'{count} sample books created successfully!')

	except Exception as e:
		print(f'Error creating contacts: {e}')

def generate_movies(count=100):
	"""
	Generates and inserts 'count' number of movies into the database.
	"""
	try:
		sample_movies = [Movie(
			title = ' '.join(fake.words(4)),
			director = fake.name(),
			format = 'DVD',
			release_year = fake.year(),
			series = ' '.join(fake.words(3)),
			series_num = fake.random_int(min=1, max=12),
			summary = fake.paragraph(),
			notes = fake.paragraph(),
			condition = 'Good'
		)
		for i in range(count)
		]

		Movie.objects.bulk_create(sample_movies)

		print(f'{count} sample movies created successfully!')

	except Exception as e:
		print(f'Error creating contacts: {e}')

def generate_tv(count=100):
	"""
	Generates and inserts 'count' number of tv shows into the database.
	"""
	try:
		sample_tv = [TV(
			title = ' '.join(fake.words(4)),
			creator = fake.name(),
			release_year = fake.year(),
			format = 'DVD',
			season = fake.random_int(min=1, max=12),
			summary = fake.paragraph(),
			notes = fake.paragraph(),
			condition = 'Good'
		)
		for i in range(count)
		]

		TV.objects.bulk_create(sample_tv)

		print(f'{count} sample tv shows created successfully!')

	except Exception as e:
		print(f'Error creating contacts: {e}')

def generate_videogames(count=100):
	"""
	Generates and inserts 'count' number of video games into the database.
	"""
	try:
		sample_videogames = [VideoGame(
			title = ' '.join(fake.words(4)),
			developer = ' '.join(fake.words(2)),
			publisher = ' '.join(fake.words(2)),
			release_year = fake.year(),
			platform = 'PlayStation 4',
			series = ' '.join(fake.words(3)),
			series_num = fake.random_int(min=1, max=12),
			summary = fake.paragraph(),
			notes = fake.paragraph(),
			condition = 'Good'
		)
		for i in range(count)
		]

		VideoGame.objects.bulk_create(sample_videogames)

		print(f'{count} sample video games created successfully!')

	except Exception as e:
		print(f'Error creating contacts: {e}')

if __name__ == '__main__':
	num_records = int(input('Enter number of entries to generate: ') or 100)
	generate_books(num_records)
	generate_movies(num_records)
	generate_tv(num_records)
	generate_videogames(num_records)

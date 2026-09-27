from django.db import models

class Book(models.Model):
	CONDITION_CHOICES = [
			('Mint', 'Mint'),
			('Near_Mint', 'Near-Mint'),
			('Good', 'Good'),
			('Poor', 'Poor')
			]

	title = models.CharField(max_length=255)
	author = models.CharField(max_length=255, blank=True)
	publisher = models.CharField(max_length=255, blank=True)
	isbn = models.CharField(max_length=20, blank=True)
	cover_url = models.URLField(blank=True)
	notes = models.TextField(blank=True)
	condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True)

	def __str__(self):
		return self.title

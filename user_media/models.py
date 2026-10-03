from django.db import models

# TODO: Determine how to handle TV Seasons

CONDITION_CHOICES = [
                ('Factory Sealed', 'Factory Sealed'),
                ('Mint', 'Mint'),
                ('Near Mint', 'Near Mint'),
                ('Great', 'Great'),
                ('Good', 'Good'),
                ('Fair', 'Fair'),
                ('Poor', 'Poor'),
                ]

class Book(models.Model):

        title = models.CharField(max_length=255)
        author = models.CharField(max_length=255, blank=True)
        publisher = models.CharField(max_length=255, blank=True)
        release_year = models.PositiveSmallIntegerField(blank=True, null=True)
        isbn = models.CharField(max_length=20, blank=True)
        series = models.CharField(max_length=255, blank=True)
        series_num = models.FloatField(blank=True, null=True)
        cover_url = models.URLField(blank=True)
        summary = models.TextField(blank=True)
        notes = models.TextField(blank=True)
        condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True)

        def __str__(self):
                return self.title

class Movie(models.Model):

        FORMAT_CHOICES = [
                        ('DVD', 'DVD'),
                        ('Blu-ray', 'Blu-ray'),
                        ('HD-DVD', 'HD-DVD'),
                        ('VHS', 'VHS'),
                        ('LaserDisc', 'LaserDisc'),
                        ('Betamax', 'Betamax')
                        ]

        title = models.CharField(max_length=255)
        director = models.CharField(max_length=255, blank=True)
        release_year = models.PositiveSmallIntegerField(blank=True, null=True)
        format = models.CharField(max_length=20, choices=FORMAT_CHOICES, blank=True)
        series = models.CharField(max_length=255, blank=True)
        series_num = models.FloatField(blank=True, null=True)
        cover_url = models.URLField(blank=True)
        summary = models.TextField(blank=True)
        notes = models.TextField(blank=True)
        condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True)

        def __str__(self):
                return self.title

class TV(models.Model):

        FORMAT_CHOICES = [
                        ('DVD', 'DVD'),
                        ('Blu-ray', 'Blu-ray'),
                        ('HD-DVD', 'HD-DVD'),
                        ('VHS', 'VHS'),
                        ('LaserDisc', 'LaserDisc'),
                        ('Betamax', 'Betamax')
                        ]

        title = models.CharField(max_length=255)
        creator = models.CharField(max_length=255, blank=True)
        release_year = models.PositiveSmallIntegerField(blank=True, null=True)
        format = models.CharField(max_length=20, choices=FORMAT_CHOICES, blank=True)
        season = models.IntegerField(blank=True, null=True)
        cover_url = models.URLField(blank=True)
        summary = models.TextField(blank=True)
        notes = models.TextField(blank=True)
        condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True)

        def __str__(self):
                return self.title

class VideoGame(models.Model):

        PLATFORM_CHOICES = [
                        ('Nintendo Switch 2', 'Nintendo Switch 2'),
                        ('Playstation 5', 'PlayStation 5'),
                        ('Xbox Series', 'Xbox Series X|S'),
                        ('Nintendo Switch', 'Nintendo Switch'),
                        ('Playstation 4', 'PlayStation 4'),
                        ('Xbox One', 'Xbox One'),
                        ('Nintendo Wii U', 'Nintendo Wii U'),
                        ('PS Vita', 'PS Vita'),
                        ('Nintendo 3DS', 'Nintendo 3DS'),
                        ('Playstation 3', 'PlayStation 3'),
                        ('Nintendo Wii', 'Nintendo Wii'),
                        ('Xbox 360', 'Xbox 360'),
                        ('PSP', 'PSP'),
                        ('Nintendo DS', 'Nintendo DS'),
                        ('Xbox', 'Xbox'),
                        ('Nintendo Gamecube', 'Nintendo Gamecube'),
                        ('Game Boy Advance', 'Game Boy Advance'),
                        ('Playstation 2', 'PlayStation 2'),
                        ('Sega Dreamcast', 'Sega Dreamcast'),
                        ('Game Boy Color', 'Game Boy Color'),
                        ('Nintendo 64', 'Nintendo 64'),
                        ('Playstation', 'PlayStation'),
                        ('Super Nintendo', 'Super Nintendo'),
                        ('Game Boy', 'Game Boy'),
                        ('Sega Genesis', 'Sega Genesis'),
                        ('NES', 'NES'),
                        ('PC', 'PC'),
                        ('Other', 'Other')
                        ]

        title = models.CharField(max_length=255)
        developer = models.CharField(max_length=255, blank=True)
        publisher = models.CharField(max_length=255, blank=True)
        release_year = models.PositiveSmallIntegerField(blank=True, null=True)
        platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES, blank=True)
        series = models.CharField(max_length=255, blank=True)
        series_num = models.FloatField(blank=True, null=True)
        cover_url = models.URLField(blank=True)
        summary = models.TextField(blank=True)
        notes = models.TextField(blank=True)
        condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, blank=True)

        def __str__(self):
                return self.title

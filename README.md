# NerdHoard 
NerdHoard is a Django application for keeping track of your stuff! Never buy a third copy of the same paperback or forget which seasons of a TV show you own again.

Example Book Hoard:
<img width="1258" height="534" alt="image" src="https://github.com/user-attachments/assets/62b2ff32-6afe-4bb8-9bfe-3de41d661724" />

## What NerdHoard does:
- Track books, movies, TV shows, and video games you own in one place
- Search your hoard
- API connections allow you to search for something and fill the add form in easily (including cover art!)
- Edit and delete whatever you want

## Setup

You'll need [conda](https://conda.io/) installed for an isolated environment

```bash
git clone https://github.com/Park-Will/NerdHoard.git
cd NerdHoard
conda create -n nerdhoard python=3.12
conda activate nerdhoard
pip install "Django>=5.2,<5.3" django-extensions requests python-dotenv
python manage.py migrate
python manage.py runserver
```
Then head to http://127.0.0.1:8000/ and start your hoard.

## API Autofill (required)
To set up the API autofill, you will need two free API keys (Open Library does not require a key):

API Information:
- **Books:** [Open Library](https://openlibrary.org/)
- **Movies and TV:** [TMDB](https://www.themoviedb.org/settings/api/request), free key
- **Video games:** [RAWG](https://rawg.io/apidocs), free key

Make a '.env' file in the project folder with the following variables:
```env
TMDB_API_KEY=<your token here>
RAWG_API_KEY=<your key here>
OPENLIBRARY_CONTACT=<your email address here>
```

- NOTE: Some information is unavailable via these APIs and will need to be entered manually.

## Test Data Fill (optional)
To check out the functionality of NerdHoard without manually adding media you will just need to install the Faker package and run the 'generate_entries.py' script
```bash
pip install Faker
python generate_entries.py
```

## Acknowledgements
- Book data from [Open Library](https://openlibrary.org/), 
- Movie and TV data from [TMDB](https://www.themoviedb.org/) *This product uses the TMDB API but is not endorsed or certified by TMDB.*
- Video game data from [RAWG](https://rawg.io/)
- Created with Django and Python
- Built for CSCI-4830 at University of Nebraska Omaha, Fall '26.

## License
MIT, see 

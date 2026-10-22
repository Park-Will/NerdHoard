# NerdHoard
NerdHoard is a Django application for keeping track of your stuff! Never buy a third copy of the same paperback or forget which seasons of a TV show you own again.

Example Book Hoard:
<img width="1243" height="662" alt="NerdHoard book collection page" src="https://github.com/user-attachments/assets/b6d8ddcf-39d1-489b-a160-90fe5c0b04a2" />

## NerdHoard Features
- Track books, movies, TV shows, and video games you own in one place
- Search your hoard
- API connections allow you to search for something and fill the add form in easily (including cover art!)
- Edit and delete whatever you want

## Setup

You'll need [conda](https://conda.io) installed for an isolated environment.

**1. Clone the repo and create conda environment**
```bash
git clone https://github.com/Park-Will/NerdHoard.git
cd NerdHoard
conda create -n nerdhoard python=3.12
conda activate nerdhoard
pip install "Django>=5.2,<5.3" django-extensions requests python-dotenv
```

**2. Get API keys**

API Information:
- **Books:** [Open Library](https://openlibrary.org/) (no key needed, just an email address in the `.env` below)
- **Movies and TV:** [TMDB](https://www.themoviedb.org/settings/api/request) (free key)
- **Video games:** [RAWG](https://rawg.io/apidocs) (free key)

Make a `.env` file in the project folder with the following variables:
```env
TMDB_API_KEY=<your key here>
RAWG_API_KEY=<your key here>
OPENLIBRARY_CONTACT=<your email address here>
```

**3. Run NerdHoard**
```bash
python manage.py migrate
python manage.py runserver
```
Then head to http://127.0.0.1:8000/ to start hoarding.

- NOTE: Some information is unavailable via these APIs and will need to be entered manually.

## Test Data (optional)
To check out the functionality of NerdHoard without manually adding media you will just need to install the Faker package and run the `generate_entries.py` script
```bash
pip install Faker
python generate_entries.py
```
Enter how many entries you would like to generate (per media type) and hit Enter (default is 100).

## Acknowledgements
- Book data from [Open Library](https://openlibrary.org/)
- Movie and TV data from [TMDB](https://www.themoviedb.org/) *NerdHoard uses the TMDB API but is not endorsed or certified by TMDB.*
- Video game data from [RAWG](https://rawg.io/)
- Created with Django and Python
- Built for CSCI-4830 at University of Nebraska Omaha, Fall '26.

## License
MIT, see [LICENSE](LICENSE) for further detail.

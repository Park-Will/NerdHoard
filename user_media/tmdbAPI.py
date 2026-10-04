import requests
from django.conf import settings

request_header = {
    'accept': 'application/json',
    'Authorization': f'Bearer {settings.TMDB_API_KEY}'
}

url = 'https://api.themoviedb.org/3/search/movie'

def movie_search(user_request, limit=5):
    response = requests.get(
        url,
        params = {
            'query': user_request,
        },
        headers = request_header,
        timeout = 10
        )
    response.raise_for_status()
    
    results = response.json()['results'][:limit]
    movie_info = [{
        'tmdb_id': r['id'],
        'title': r['title'],
        'release_date': r.get('release_date') or None,
        'summary': r.get('overview', ''),
        'cover_url': (
            f'https://image.tmdb.org/t/p/w500{r["poster_path"]}'
            if r.get('poster_path') else ''
        ),
    }
    for r in results
    ]

    return movie_info

def movie_details(tmdb_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/movie/{tmdb_id}',
        params = {'append_to_response': 'credits'},
        headers = request_header,
        timeout = 10,
    )
    response.raise_for_status()
    details = response.json()
    directors = []
    for i in details.get('credits', {}).get('crew', []):
        if i.get('job') == 'Director':
            directors.append(i['name'])
    return {'director': ', '.join(directors)}
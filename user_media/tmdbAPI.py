import requests
from django.conf import settings

request_header = {
    'accept': 'application/json',
    'Authorization': f'Bearer {settings.TMDB_API_KEY}'
}

def movie_search(user_request, limit=5):
    response = requests.get(
        'https://api.themoviedb.org/3/search/movie',
        params = {
            'query': user_request,
        },
        headers = request_header,
        timeout = 10
        )
    response.raise_for_status()
    
    results = response.json()['results'][:limit]
    movie_info = [{
        'tmdb_id': result['id'],
        'title': result['title'],
        'release_date': result.get('release_date') or None,
        'summary': result.get('overview', ''),
        'cover_url': (
            f'https://image.tmdb.org/t/p/w500{r["poster_path"]}'
            if result.get('poster_path') else ''
        ),
    }
    for result in results
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

def tv_search(user_request, limit=5):
    response = requests.get(
        'https://api.themoviedb.org/3/search/tv',
        params = {
            'query': user_request,
        },
        headers = request_header,
        timeout = 10
        )
    response.raise_for_status()
    
    results = response.json()['results'][:limit]
    tv_info = [{
        'tmdb_id': result['id'],
        'title': result['name'],
        'release_date': result.get('first_air_date') or None,
        'summary': result.get('overview', ''),
        'cover_url': (
            f'https://image.tmdb.org/t/p/w500{result["poster_path"]}'
            if result.get('poster_path') else ''
        ),
    }
    for result in results
    ]

    return tv_info

def tv_details(tmdb_id):
    response = requests.get(
        f'https://api.themoviedb.org/3/tv/{tmdb_id}',
        headers = request_header,
        timeout = 10,
    )
    response.raise_for_status()
    details = response.json()
    creators = [creator['name'] for creator in details.get('created_by', [])]
    return {'created_by': ', '.join(creators)}
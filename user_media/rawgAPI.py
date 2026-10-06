import requests
from django.conf import settings

base_url = 'https://api.rawg.io/api/games'

def game_search(user_request, limit=5):
    response = requests.get(
        base_url,
        params={
            'key': settings.RAWG_API_KEY,
            'search': user_request,
        },
        timeout = 10
        )
    response.raise_for_status()

    results = response.json()['results'][:limit]
    game_info = [{
        'rawg_id': result['id'],
        'title': result['name'],
        'release_year': int(result['released'][:4]) if result.get('released') else None,
        'cover_url': result.get('background_image') or '',
    }
    for result in results
    ]

    return game_info

def game_details(rawg_id):
    response = requests.get(
        f'{base_url}/{rawg_id}',
        params = {'key': settings.RAWG_API_KEY},
        timeout = 10,
    )
    response.raise_for_status()
    details = response.json()
    developers = [dev['name'] for dev in details.get('developers', [])]
    publishers = [pub['name'] for pub in details.get('publishers', [])]
    return {
        'summary': details.get('description_raw', ''),
        'developer': ', '.join(developers),
        'publisher': ', '.join(publishers),
    }
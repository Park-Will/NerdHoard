import requests
from django.conf import settings

request_header = {'User-Agent': f'NerdHoard/0.1 ({settings.OPENLIBRARY_CONTACT})'}

def book_search(user_request, limit=5):
    response = requests.get(
        'https://openlibrary.org/search.json',
        params = {
            'q': user_request,
            'limit': limit,
            'fields': 'key,title,author_name,first_publish_year,cover_i'
        },
        headers = request_header,
        timeout = 10
        )
    response.raise_for_status()

    book_info = []
    for i in response.json().get('docs', []):
        book_info.append({
            'title': i.get('title', ''),
            'author': ', '.join(i.get('author_name', [])),
            'release_year': i.get('first_publish_year'),
            'cover_url': (f'https://covers.openlibrary.org/b/id/{i["cover_i"]}-M.jpg' if i.get('cover_i') else None),
            'openlibrary_key': i.get('key')
        })
    
    return book_info

def book_summary(openlibrary_key):
    response = requests.get(
        f'https://openlibrary.org{openlibrary_key}.json',
        headers = request_header,
        timeout = 10
    )
    response.raise_for_status()
    description = response.json().get('description', '')
    if hasattr(description, 'get'):
        description = description.get('value', '')
    return description

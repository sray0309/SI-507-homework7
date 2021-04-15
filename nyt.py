import secrets
import requests
import json

url = f'https://api.nytimes.com/svc/topstories/v2/technology.json?api-key={secrets.key}'

response = requests.get(url)
results = response.json()['results']

top5 = []
for i in range(5):
    top5.append({
        'title': results[i]['title'],
        'url': results[i]['url']
    })
    for media in results[i]['multimedia']:
        if media['format'] == 'Standard Thumbnail':
            top5[i]['thumbnail_url'] = media['url']
            break

print(top5)
import requests

chunk_size = 256
url = 'link.mp4'
r = requests.get(url, stream=True)

with open('name.mp4', 'wb') as f:
    for chunk in r.iter_content(chunk_size):
        f.write(chunk)

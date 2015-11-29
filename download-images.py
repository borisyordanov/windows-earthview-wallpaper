import json
import image_scraper
import requests
import re


with open('earthview.json') as data_file:    
    data = json.load(data_file)
    for i in data:
        r = requests.get(i['image'], allow_redirects=True)
        split_url = i['image'].split('/')
        filename = split_url[len(split_url) - 1]
        open('images/' + filename, 'wb').write(r.content)

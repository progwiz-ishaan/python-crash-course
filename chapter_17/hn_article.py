import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Explore the struture of the data.
response_dict = r.json()
readble_file = '/home/ishaan/Documents/Ishaan\'s-Coding/python-crash-course/chapter_17/data/readable_hn_data.json'
with open(readble_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
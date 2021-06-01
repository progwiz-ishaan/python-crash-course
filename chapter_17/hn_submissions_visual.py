from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline

import requests

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a sepreate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/27344010.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dict for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/v0/item/{submission_id}",
        'comments': response_dict['descendants']
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), \
reverse=True)
comments, names = [], []

for submission_dict in submission_dicts:
    comments.append(submission_dict['comments'])
    names.append(submission_dict['title'])

# Make Visualizion
data = [{
    'type': 'data',
    'x': names,
    'y': comments
}]
my_layout = {
    'title': 'The Most Active Headlines of Today',
    'xaxis': {'title': 'Headline Titles'},
    'yaxis': {'title': 'Comments'}
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='headlines.html')
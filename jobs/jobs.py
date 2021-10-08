from django.conf import settings

import json
import requests

def get_latest_news():
    
    """This function retrieves the 100 newest stories published on the hacker news website"""

    url = 'https://hacker-news.firebaseio.com/v0/newstories.json'
    response = requests.get(url).json()
    if response:
        new_stories = response[0:99]
        print(new_stories)


def save_news_to_DB():
    url = 'https://hacker-news.firebaseio.com/v0/newstories.json'
    response = requests.get(url).json()
    if response:
        new_stories = response[0:99]
        # print(new_stories)

    for id in new_stories:
        if id in new_stories:
            return id
    
    story_url = 'https://hacker-news.firebaseio.com/v0/item/{item_id}.json'

    story_response = requests.get(story_url.format(item_id=id)).json()
    print(story_response)
    # title = story_response{'title'}
    # print(title)

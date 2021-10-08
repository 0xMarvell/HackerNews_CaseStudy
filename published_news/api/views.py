from django.http.response import JsonResponse
import requests
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def save_news_to_DB(request, id):
    url = 'https://hacker-news.firebaseio.com/v0/newstories.json'
    response = requests.get(url).json()
    if response:
        new_stories = response[0:99]

    if id in new_stories:
        story_url = 'https://hacker-news.firebaseio.com/v0/item/{item_id}.json'

        story_response = requests.get(story_url.format(item_id=id)).json()
        print(story_response)
        return Response(story_response)
    else:
        return Response({"Error":"This story isn't a part of the latest 100"})

    


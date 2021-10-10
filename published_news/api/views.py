from django.http.response import JsonResponse
import requests
import json

from rest_framework.decorators import api_view
from rest_framework.response import Response

from published_news.models import PublishedNews

@api_view(['GET'])
def save_news_to_DB(request):

    """This function retrieves the JSON data for each story and saves it to the database.
    Take note that it ony retrieves data for the 100 newest published stories on the website."""

    all_news = {}
    url = 'https://hacker-news.firebaseio.com/v0/newstories.json'
    response = requests.get(url).json()
    if response:
        new_stories = response[0:99]

    for id in new_stories:
        story_url = 'https://hacker-news.firebaseio.com/v0/item/{item_id}.json'

        story_response = requests.get(story_url.format(item_id=id)).json()
        print(story_response)
        
        for story_data in story_response:
            story_data = PublishedNews(
            title= story_response['title'],
            url= story_response['url'],
            by= story_response['by'],
            score= story_response['score'],
            item_type= story_response['type'],
            descendants= story_response['descendants']
            )
            story_data.save()
            all_news = PublishedNews.objects.all().order_by('-id')
        return Response(all_news.json())
    else:
        return Response({"Error":"Retrieve operation failed. This story isn't a part of the 100 newest published stories"})



    


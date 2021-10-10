import json
import requests

from django.conf import settings

from published_news.models import PublishedNews


def get_latest_news():
    
    """This function retrieves the 100 newest stories published on the hacker news website.
    It returns a list of story IDs."""

    url = 'https://hacker-news.firebaseio.com/v0/newstories.json'
    response = requests.get(url).json()
    if response:
        new_stories = response[0:99]
        print(new_stories)


def save_news_to_DB():

    """This function retrieves the JSON data for each story and saves it to the database.
    Take note that it ony retrieves data for the 100 newest published stories on the website."""

    all_news = {}
    url = 'https://hacker-news.firebaseio.com/v0/newstories.json'
    r = requests.get(url)
    article_ids = r.json()
    # if response:
    #     new_stories = response[0:100]

    for article_id in article_ids[:50]:
        story_url = 'https://hacker-news.firebaseio.com/v0/item/{item_id}.json'
        story_response = requests.get(story_url.format(item_id=article_id)) # get response for each story
        one_article = story_response.json()

        story_data = PublishedNews(
            title= one_article['title'],
            url= one_article['url'],
            by= one_article['by'],
            score= one_article['score'],
            item_type= one_article['type'],
            comments= one_article['descendants']
            )
        # print(story_data.objects.all())
        if str(story_data.title) not in str(list(PublishedNews.objects.all())):
            story_data.save()
        else:
            print('already in db')
            continue
        all_news = PublishedNews.objects.all().order_by('-id')
        print(all_news)
        # print()
        
    # for story_data in story_response:



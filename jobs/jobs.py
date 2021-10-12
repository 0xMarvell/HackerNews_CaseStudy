import json
import requests

from django.conf import settings

from published_news.models import PublishedNew, Comment

# I used this piece of code to test how to get the list of IDs for the latest stories

# def get_latest_news():
    
#     """This function retrieves the 100 newest stories published on the hacker news website.
#     It returns a list of story IDs."""

#     url = 'https://hacker-news.firebaseio.com/v0/newstories.json'
#     response = requests.get(url).json()
#     if response:
#         new_stories = response[0:99]
#         print(new_stories)


def save_news_to_DB():

    """This function retrieves the JSON data for each story and saves it to the database.
    Take note that it ony retrieves data for the 50 newest published stories on the website."""

    all_news = {}
    url = 'https://hacker-news.firebaseio.com/v0/newstories.json'
    r = requests.get(url)
    article_ids = r.json()

    for article_id in article_ids[:100]:
        story_url = 'https://hacker-news.firebaseio.com/v0/item/{item_id}.json'
        story_response = requests.get(story_url.format(item_id=article_id)) # get response for each story
        one_article = story_response.json()

        story_data = PublishedNew(
            title= one_article['title'],
            url= one_article['url'],
            by= one_article['by'],
            score= one_article['score'],
            item_type= one_article['type'],
            comments= one_article['descendants'],
            hacker_news_id= one_article['id']
            )
            
        if str(story_data.title) not in str(list(PublishedNew.objects.all())): #if the retrieved data does not exist in the local database
            story_data.save() 
        else:
            print('already in db')
            continue # skip over any retrieved data already saved in the database and keep looping
        all_news = PublishedNew.objects.all().order_by('-id')
        print(all_news)


def save_comments_to_DB():

    """This function retrieves the JSON data for the comments (with the key "kids") connected 
    to each published story and saves it to the database.
    Take note that it ony retrieves data for the 50 newest published stories on the website."""

    all_comments = {}

    new_stories_url = 'https://hacker-news.firebaseio.com/v0/newstories.json'
    new_stories_r = requests.get(new_stories_url)
    article_ids = new_stories_r.json()[:100]

    for article_id in article_ids:
        url = 'https://hacker-news.firebaseio.com/v0/item/{item_id}/kids.json'
        r = requests.get(url.format(item_id=article_id))
        comment_ids = r.json()

        if comment_ids is not None:
            for comment_id in comment_ids:
                comment_url = 'https://hacker-news.firebaseio.com/v0/item/{item_id}.json'
                comment_response = requests.get(comment_url.format(item_id=comment_id)) # get response for each comment
                one_comment = comment_response.json()

                comment_data = Comment(
                    text= one_comment['text'],
                    by= one_comment['by'],
                    item_type= one_comment['type'],
                    parent_id= one_comment['parent']
                    )
                    
                if str(comment_data.text) not in str(list(Comment.objects.all())): #if the retrieved data does not exist in the local database
                    comment_data.save() 
                else:
                    print('already in db')
                    continue # skip over any retrieved data already saved in the database and keep looping
                all_comments = Comment.objects.all().order_by('-id')
                print(all_comments)
        else:
            print('no comments for this story')


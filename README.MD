# A case study on the Hacker News website API

<h4>The challenge was to make a website that fetches data from the Hacker News API and perform various tasks with it</h4>
</br>

## Tasks:

1. Choose a web framework of your choice. Django, Flask, use what you like. Make a new virtualenv and pip install it;
2. Make a scheduled job to sync the published news to a DB every 5 minutes. You can start with the latest 100 items, and sync every new item from there. Note: here are several types of news (items), with relations between them;
3. Implement a view to list the latest news;
4. Allow filtering by the type of item;
5. Implement a search box for filtering by text;
6. As there are hundreds of news you probably want to use pagination or lazy loading when you display them.

### It is also important to expose an API so that our data can be consumed:

7. GET : List the items, allowing filters to be specified;
8. POST : Add new items to the database (not present in Hacker News);


<b>Project Setup</b>
<ul>
    <li>clone Project or download as zip file - 
        <code>git clone https://github.com/Marvellous-Chimaraoke/HackerNews_CaseStudy.git</code>
    </li>
    <li>Create virtual environment - 
        <code>pip3 install virtualenv</code>
        then run <code>virtualenv env</code>, 
        <code>source env/bin/activate</code>(for mac/linux), 
        <code>env/scripts/activate.bat</code>(for windows)
     </li>
    <li>install all requirements from requirements.txt file - 
        <code>pip install -r requirements.txt</code>
    </li>
    <li>Run migrations to create db tables - 
        <code>python manage.py makemigrations</code> 
        then run <code>python manage.py migrate</code>
    </li> 
</ul>

</br>

<b>Run Project Server</b>
<ul>
    <li>
    <code>python manage.py runserver --noreload</code>
    </li>
</ul>

### API ENDPOINTS
1. GET - ```http://127.0.0.1:8000/api/news/```
   
   Returns - All news objects saved in the database

   POST - `http://127.0.0.1:8000/api/news/`
   payload - 
       ```{
        "title": string,
        "url": url,
        "by": string,
        "score": int,
        "item_type": string
    }```

    Returns - The newly created news object

2. GET - `http://127.0.0.1:8000/api/news?{filter}={filter_value}`
   
   Returns - Filtered news objects

3. PUT/PATCH - `http://127.0.0.1:8000/api/news/{pk}/update`
   payload (PUT) - `{
        "title": "Updated value",
        "url": "Updated value",
        "by": "Updated value",
        "score": Updated value,
        "item_type": "Updated value",
        "comments": Updated value,
        "hacker_news_id": Updated value
    }`

    payload (PATCH) - `{
        "key": "Updated value"
    }`

    Returns - Updated news object

4. DELETE - `http://127.0.0.1:8000/api/news/{pk}/delete`
   
   Returns - Deleted news object

5. GET - `http://127.0.0.1:8000/api/news/comments`
   
   Returns - All comment objects saved in the databse

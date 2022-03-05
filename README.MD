# A CASE STUDY ON THE HACKERNEWS API

## TASKS

### PART 1
Build a website that fetches data from the Hacker News API and perform various tasks with it:
 - Choose a web framework of your choice. Django, Flask, use what you like. Make a new virtualenv and pip install it.
 - Make a scheduled job to sync the published news to a DB every 5 minutes. You can start with the latest 100 items, and sync every new item from there.
    - Note: here are several types of news (items), with relations between them.
 - Implement a view to list the latest news.
 - Allow filtering by the type of item.
 - Implement a search box for filtering by text.
 - As there are hundreds of news you probably want to use pagination or lazy loading when you display them.

### PART 2
It is also important to expose an API so that our data can be consumed:
 - ```GET``` : List the items, allowing filters to be specified.
 - ```POST``` : Add new items to the database (not present in Hacker News).


## PROJECT SETUP
 - clone Project or download as zip file.
 ```bash
 git clone https://github.com/Marvellous-Chimaraoke/HackerNews_CaseStudy.git
 ```
 - Create virtual environment.
```bash
pip3 install virtualenv
virtualenv env
```
- Activate virtual environment (MacOS/Linux).
```bash
source env/bin/activate
``` 
- Activate virtual environment (Windows).
```bash
env/scripts/activate.bat
```   
 - Install all requirements from requirements.txt file.
 ```bash
 pip install -r requirements.txt
 ```
 - Run migrations to create database tables.
 ```bash
 python manage.py makemigrations
 python manage.py migrate
 ```
 - Run Project Server.
 ```bash
 python manage.py runserver --noreload
 ```

Take a look at the API endpoints [here](./published_news/api)

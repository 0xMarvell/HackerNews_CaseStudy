from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import save_news_to_DB, save_comments_to_DB

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(save_news_to_DB, 'interval', minutes=5)
	scheduler.add_job(save_comments_to_DB, 'interval', minutes=5)
	scheduler.start()
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import save_news_to_DB

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(save_news_to_DB, 'interval', seconds=10)
	scheduler.start()
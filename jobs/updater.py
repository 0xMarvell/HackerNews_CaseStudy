from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .jobs import get_latest_news

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(get_latest_news, 'interval', seconds=5)
	scheduler.start()
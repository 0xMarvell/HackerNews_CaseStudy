from django.apps import AppConfig


class PublishedNewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'published_news'

    # def ready(self):
    # 	from jobs import updater
    # 	updater.start()

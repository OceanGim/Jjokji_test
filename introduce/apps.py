from unicodedata import name
from django.apps import AppConfig


class IntroduceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'introduce'

class AccessLogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'AccessLog'
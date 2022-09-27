from django.db import models
from django.forms import DateTimeField

# Create your models here.
class AccessLog(models.Model):
    create_at = models.DateTimeField("생성 시간", auto_now_add=True)
    location = models.CharField("접속 경로", max_length=50)

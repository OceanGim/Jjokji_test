from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class AccessLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.charfield(max_lenth=100)
    
    def __str__(self):
        return self.created_at
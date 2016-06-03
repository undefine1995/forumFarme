from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class activeCode(models.Model):
    ower = models.ForeignKey(User, verbose_name='持有者')
    Code = models.CharField(max_length = 255)
    expiry_time = models.DateTimeField()

    create_timestmp = models.DateTimeField(auto_now_add = True)
    last_timestmp = models.DateTimeField(auto_now = True)

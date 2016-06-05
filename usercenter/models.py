#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ActivateCode(models.Model):
    ower = models.ForeignKey(User, verbose_name='持有者')
    Code = models.CharField(max_length = 255)
    expiry_ti = models.DateTimeField()

    create_timestmp = models.DateTimeField(auto_now_add = True)
    last_timestmp = models.DateTimeField(auto_now = True)

#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Block(models.Model):
    title = models.CharField(u'名称',max_length = 40)
    describe = models.CharField(u'描述',max_length = 1000)
    ower = models.ForeignKey(User,verbose_name = u'管理员')

    create_timestamp = models.DateTimeField(auto_now_add = True)
    last_update_timestamp = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = u'版块'
        verbose_name_plural = u'版块'

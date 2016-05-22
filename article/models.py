#coding:utf-8
from django.db import models
from django.contrib.auth.models import User
from block.models import Block
# Create your models here.

class Article(models.Model):
    block = models.ForeignKey(Block,verbose_name = u'所属版块')
    ower = models.ForeignKey(User,verbose_name = u'作者')
    title = models.CharField(u'标题', max_length = 200)
    content = models.CharField(u'内容', max_length = 10000)
    status = models.IntegerField(u'状态', choices = ((0,u'普通'), (-1,u'删除'), (10,u'精华')), default = 0)

    create_timestmp = models.DateTimeField(auto_now_add = True)
    last_timestmp = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'文章'
        verbose_name_plural = u'文章'


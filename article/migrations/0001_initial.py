# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('block', '0002_auto_20160522_0350'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='\u6807\u9898')),
                ('content', models.CharField(max_length=10000, verbose_name='\u5185\u5bb9')),
                ('status', models.IntegerField(default=0, verbose_name='\u72b6\u6001', choices=[(0, '\u666e\u901a'), (-1, '\u5220\u9664'), (10, '\u7cbe\u534e')])),
                ('create_timestmp', models.DateTimeField(auto_now_add=True)),
                ('last_timestmp', models.DateTimeField(auto_now=True)),
                ('block', models.ForeignKey(verbose_name='\u6240\u5c5e\u7248\u5757', to='block.Block')),
                ('ower', models.ForeignKey(verbose_name='\u4f5c\u8005', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u6587\u7ae0',
                'verbose_name_plural': '\u6587\u7ae0',
            },
        ),
    ]

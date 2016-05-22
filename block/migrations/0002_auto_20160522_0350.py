# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('block', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'verbose_name': '\u7248\u5757', 'verbose_name_plural': '\u7248\u5757'},
        ),
        migrations.AlterField(
            model_name='block',
            name='describe',
            field=models.CharField(max_length=1000, verbose_name='\u63cf\u8ff0'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivateCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Code', models.CharField(max_length=255)),
                ('expiry_time', models.DateTimeField()),
                ('create_timestmp', models.DateTimeField(auto_now_add=True)),
                ('last_timestmp', models.DateTimeField(auto_now=True)),
                ('ower', models.ForeignKey(verbose_name=b'\xe6\x8c\x81\xe6\x9c\x89\xe8\x80\x85', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercenter', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activatecode',
            old_name='expiry_time',
            new_name='expiry_ti',
        ),
    ]

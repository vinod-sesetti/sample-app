# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150716_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='email',
            field=models.EmailField(default=datetime.datetime(2015, 7, 17, 10, 17, 37, 271833, tzinfo=utc), unique=True, max_length=75),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=75),
            preserve_default=True,
        ),
    ]

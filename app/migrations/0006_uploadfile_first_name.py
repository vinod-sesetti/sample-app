# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150720_0718'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfile',
            name='first_name',
            field=models.CharField(default=datetime.datetime(2015, 7, 20, 8, 35, 20, 486118, tzinfo=utc), max_length=20),
            preserve_default=False,
        ),
    ]

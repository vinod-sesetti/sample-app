# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job', models.IntegerField(editable=False)),
                ('dist', models.DecimalField(max_digits=10, decimal_places=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

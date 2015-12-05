# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20151205_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='finished_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

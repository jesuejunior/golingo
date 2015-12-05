# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='level',
            name='unity',
        ),
        migrations.RemoveField(
            model_name='result',
            name='total',
        ),
        migrations.AddField(
            model_name='unity',
            name='level',
            field=models.IntegerField(default=1, verbose_name='Level'),
        ),
        migrations.AlterField(
            model_name='question',
            name='lesson',
            field=models.ForeignKey(to='quiz.Lesson', verbose_name='Lesson', related_name='questions'),
        ),
        migrations.DeleteModel(
            name='Level',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_result_finished_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='correct',
            field=models.IntegerField(default=0, verbose_name='Respostas corretas'),
        ),
        migrations.AlterField(
            model_name='result',
            name='lesson',
            field=models.ForeignKey(to='quiz.Lesson', related_name='results'),
        ),
        migrations.AlterField(
            model_name='result',
            name='wrong',
            field=models.IntegerField(default=0, verbose_name='Respostas erradas'),
        ),
    ]

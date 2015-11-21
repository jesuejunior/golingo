# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20151121_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='extra',
            field=models.CharField(max_length=255, verbose_name='Other answer', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Answer'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='media',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='unity',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Nome'),
        ),
    ]

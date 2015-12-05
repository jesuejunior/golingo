# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20151205_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Dificuldade', max_length=120)),
                ('unity', models.ForeignKey(to='quiz.Unity', verbose_name='Unidade')),
            ],
        ),
    ]

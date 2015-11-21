# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unity',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('number', models.IntegerField(unique=True, verbose_name='Unidade')),
                ('name', models.CharField(max_length='120', verbose_name='Nome')),
                ('description', models.TextField(null=True, blank=True, verbose_name='Descrição')),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='description',
            field=models.TextField(null=True, blank=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(null=True, related_name='answers', blank=True, to='quiz.Answer', db_table='question_has_answer', default=None),
        ),
        migrations.AddField(
            model_name='lesson',
            name='unity',
            field=models.ForeignKey(null=True, blank=True, to='quiz.Unity', verbose_name='Unidade'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20151121_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(null=True, blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='unity',
            field=models.ForeignKey(blank=True, null=True, to='quiz.Unity', verbose_name='Unity'),
        ),
        migrations.AlterField(
            model_name='media',
            name='name',
            field=models.CharField(max_length=40, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_correct',
            field=models.ForeignKey(to='quiz.Answer', verbose_name='Correct answer'),
        ),
        migrations.AlterField(
            model_name='question',
            name='lesson',
            field=models.ForeignKey(to='quiz.Lesson', verbose_name='Lesson'),
        ),
        migrations.AlterField(
            model_name='question',
            name='name',
            field=models.TextField(verbose_name='Question'),
        ),
        migrations.AlterField(
            model_name='unity',
            name='description',
            field=models.TextField(null=True, blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='unity',
            name='name',
            field=models.CharField(max_length=120, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='unity',
            name='number',
            field=models.IntegerField(unique=True, verbose_name='Unity'),
        ),
    ]

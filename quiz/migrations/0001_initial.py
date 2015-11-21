# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='Resposta', max_length='255')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='Nome', max_length='40')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(verbose_name='Nome', max_length='40')),
                ('url', models.URLField(verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.TextField(verbose_name='Pergunta')),
                ('answer_correct', models.ForeignKey(to='quiz.Answer', verbose_name='Resposta correta')),
                ('answers', models.ManyToManyField(null=True, to='quiz.Answer', blank=True, db_table='question_has_answer', related_name='answerss')),
                ('audio', models.ForeignKey(null=True, blank=True, to='quiz.Media', related_name='audio', on_delete=django.db.models.deletion.DO_NOTHING)),
                ('image', models.ForeignKey(null=True, blank=True, to='quiz.Media', related_name='image', on_delete=django.db.models.deletion.DO_NOTHING)),
                ('lesson', models.ForeignKey(to='quiz.Lesson', verbose_name='Liçào')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('correct', models.IntegerField(verbose_name='Respostas corretas')),
                ('wrong', models.IntegerField(verbose_name='Respostas erradas')),
                ('total', models.IntegerField(verbose_name='Total de perguntas')),
                ('lesson', models.ForeignKey(to='quiz.Lesson')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

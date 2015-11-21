from django.contrib.auth.models import User
from django.db import models


class Answer(models.Model):
    name = models.CharField(verbose_name='Resposta', max_length='255')


class Lesson(models.Model):
    name = models.CharField(verbose_name='Nome', max_length='40')


class Media(models.Model):
    name = models.CharField(verbose_name='Nome', max_length='40')
    url = models.URLField(verbose_name='URL')


class Question(models.Model):
    name = models.TextField(verbose_name='Pergunta')
    answers = models.ManyToManyField(Answer, related_name='answerss', db_table='question_has_answer', null=True, blank=True)
    answer_correct = models.ForeignKey(Answer, verbose_name='Resposta correta')
    lesson = models.ForeignKey(Lesson, verbose_name=u'Liçào')
    audio = models.ForeignKey(Media, related_name='audio', blank=True, null=True, on_delete=models.DO_NOTHING)
    image = models.ForeignKey(Media, related_name='image', blank=True, null=True, on_delete=models.DO_NOTHING)


class Result(models.Model):
    user = models.ForeignKey(User)
    lesson = models.ForeignKey(Lesson)
    correct = models.IntegerField(verbose_name='Respostas corretas')
    wrong = models.IntegerField(verbose_name='Respostas erradas')
    total = models.IntegerField(verbose_name='Total de perguntas')
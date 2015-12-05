from django.contrib.auth.models import User
from django.db import models


class Unity(models.Model):
    name = models.CharField(verbose_name='Name', max_length=120)
    number = models.IntegerField(verbose_name='Unity', unique=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)

    def __str__(self):
        return self.name


class Answer(models.Model):
    name = models.CharField(verbose_name='Answer', max_length=255)
    extra = models.CharField(verbose_name='Other answer', max_length=255, null=True, blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.extra)


class Lesson(models.Model):
    name = models.CharField(verbose_name='Name', max_length=40)
    unity = models.ForeignKey(Unity, verbose_name='Unity', null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)

    def __str__(self):
        return "Unity: {0} - Lesson: {1}".format(self.unity.name, self.name)


class Media(models.Model):
    name = models.CharField(verbose_name='Name', max_length=40)
    url = models.URLField(verbose_name='URL')

    def __str__(self):
        return self.name


class Question(models.Model):
    name = models.TextField(verbose_name='Question')
    answers = models.ManyToManyField(Answer, related_name='answers', db_table='question_has_answer', default=None,
                                     null=True, blank=True)
    answer_correct = models.ForeignKey(Answer, verbose_name='Correct answer')
    lesson = models.ForeignKey(Lesson, verbose_name=u'Lesson')
    audio = models.ForeignKey(Media, related_name='audio', blank=True, null=True, on_delete=models.DO_NOTHING)
    image = models.ForeignKey(Media, related_name='image', blank=True, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Result(models.Model):
    user = models.ForeignKey(User)
    lesson = models.ForeignKey(Lesson)
    correct = models.IntegerField(verbose_name='Respostas corretas')
    wrong = models.IntegerField(verbose_name='Respostas erradas')
    total = models.IntegerField(verbose_name='Total de perguntas')

    def __str__(self):
        return self.user.username

# encoding: utf-8
__author__ = 'jesuejunior'
from quiz.models import Unity, Answer, Lesson, Media
from unittest import TestCase
from django.db import models


class UnityModelTest(TestCase):

    def test_name_field(self):
        unity = Unity._meta.get_field_by_name('name')[0]
        self.assertEquals(unity.__class__, models.CharField)
        self.assertEquals(unity.max_length, 120)
        self.assertFalse(unity.null)
        self.assertFalse(unity.blank)

    def test_number_field(self):
        unity = Unity._meta.get_field_by_name('number')[0]
        self.assertEquals(unity.__class__, models.IntegerField)
        self.assertTrue(unity.unique)

    def test_description_field(self):
        unity = Unity._meta.get_field_by_name('description')[0]
        self.assertEquals(unity.__class__, models.TextField)
        self.assertTrue(unity.null)
        self.assertTrue(unity.blank)


class AnswerModelTest(TestCase):

    def test_name_field(self):
        answer = Answer._meta.get_field_by_name('name')[0]
        self.assertEquals(answer.__class__, models.CharField)
        self.assertEquals(answer.max_length, 255)

    def test_extra_field(self):
        answer = Answer._meta.get_field_by_name('extra')[0]
        self.assertEquals(answer.__class__, models.CharField)
        self.assertEquals(answer.max_length, 255)
        self.assertTrue(answer.null)
        self.assertTrue(answer.blank)


class LessonModelTest(TestCase):

    name = models.CharField(verbose_name='Name', max_length=40)
    unity = models.ForeignKey(Unity, verbose_name='Unity', null=True, blank=True)
    description = models.TextField(verbose_name='Description', null=True, blank=True)

    def test_name_field(self):
        lesson = Lesson._meta.get_field_by_name('name')[0]
        self.assertEquals(lesson.__class__, models.CharField)
        self.assertEquals(lesson.max_length, 40)
        self.assertFalse(lesson.blank)
        self.assertFalse(lesson.null)

    def test_unity_field(self):
        lesson = Lesson._meta.get_field_by_name('unity')[0]
        self.assertEquals(lesson.__class__, models.ForeignKey)

    def test_description_field(self):
        lesson = Unity._meta.get_field_by_name('description')[0]
        self.assertEquals(lesson.__class__, models.TextField)
        self.assertTrue(lesson.null)
        self.assertTrue(lesson.blank)


class MediaModelTest(TestCase):

    def test_name_field(self):
        media = Lesson._meta.get_field_by_name('name')[0]
        self.assertEquals(media.__class__, models.CharField)
        self.assertEquals(media.max_length, 40)
        self.assertFalse(media.blank)
        self.assertFalse(media.null)

    def test_url_field(self):
        media = Lesson._meta.get_field_by_name('url')[0]
        self.assertEquals(media.__class__, models.URLField)


class Question(TestCase):
    name = models.TextField(verbose_name='Question')
    answers = models.ManyToManyField(Answer, related_name='answers', db_table='question_has_answer', default=None,
                                     null=True, blank=True)
    answer_correct = models.ForeignKey(Answer, verbose_name='Correct answer')
    lesson = models.ForeignKey(Lesson, verbose_name=u'Lesson')
    audio = models.ForeignKey(Media, related_name='audio', blank=True, null=True, on_delete=models.DO_NOTHING)
    image = models.ForeignKey(Media, related_name='image', blank=True, null=True, on_delete=models.DO_NOTHING)

    def test_name_field(self):
        media = Media._meta.get_field_by_name('name')[0]
        self.assertEquals(media.__class__, models.TextField)
        self.assertFalse(media.blank)
        self.assertFalse(media.null)

    def test_answers_field(self):
        media = Media._meta.get_field_by_name('answers')[0]
        
# encoding: utf-8
from model_mommy import mommy
import pytest
from quiz.models import Unity, Answer, Lesson, Media, Question, Result
from unittest import TestCase
from django.db import models


class UnityModelTest(TestCase):

    def test_name_field(self):
        name = Unity._meta.get_field_by_name('name')[0]
        self.assertEquals(name.__class__, models.CharField)
        self.assertEquals(name.max_length, 120)
        self.assertFalse(name.null)
        self.assertFalse(name.blank)

    def test_number_field(self):
        number = Unity._meta.get_field_by_name('number')[0]
        self.assertEquals(number.__class__, models.IntegerField)
        self.assertTrue(number.unique)

    def test_description_field(self):
        description = Unity._meta.get_field_by_name('description')[0]
        self.assertEquals(description.__class__, models.TextField)
        self.assertTrue(description.null)
        self.assertTrue(description.blank)

    @pytest.mark.django_db
    def test_get_lessons(self):
        unity = mommy.make(Unity, id=12)
        mommy.make(Lesson, name='lesson 1', unity=unity)
        self.assertTrue(unity.get_lessons, ['lesson 1'])
        

    def test_level_field(self):
        level = Unity._meta.get_field_by_name('level')[0]
        self.assertEquals(level.__class__, models.IntegerField)
        self.assertEquals(level.default, 1)
        self.assertFalse(level.blank)
        self.assertFalse(level.null)


class AnswerModelTest(TestCase):

    def test_name_field(self):
        name = Answer._meta.get_field_by_name('name')[0]
        self.assertEquals(name.__class__, models.CharField)
        self.assertEquals(name.max_length, 255)

    def test_extra_field(self):
        answer = Answer._meta.get_field_by_name('extra')[0]
        self.assertEquals(answer.__class__, models.CharField)
        self.assertEquals(answer.max_length, 255)
        self.assertTrue(answer.null)
        self.assertTrue(answer.blank)


class LessonModelTest(TestCase):

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
        name = Media._meta.get_field_by_name('name')[0]
        self.assertEquals(name.__class__, models.CharField)
        self.assertEquals(name.max_length, 40)
        self.assertFalse(name.blank)
        self.assertFalse(name.null)

    def test_url_field(self):
        url = Media._meta.get_field_by_name('url')[0]
        self.assertEquals(url.__class__, models.URLField)


class QuestionModelTest(TestCase):
    # lesson = models.ForeignKey(Lesson, verbose_name=u'Lesson')
    # audio = models.ForeignKey(Media, related_name='audio', blank=True, null=True, on_delete=models.DO_NOTHING)
    # image = models.ForeignKey(Media, related_name='image', blank=True, null=True, on_delete=models.DO_NOTHING)

    def test_name_field(self):
        name = Question._meta.get_field_by_name('name')[0]
        self.assertEquals(name.__class__, models.TextField)
        self.assertFalse(name.blank)
        self.assertFalse(name.null)

    def test_answers_field(self):
        answers = Question._meta.get_field_by_name('answers')[0]
        self.assertEquals(answers.__class__, models.ManyToManyField)
        self.assertTrue(answers.blank)
        self.assertTrue(answers.null)

    def test_answer_correct_field(self):
        answer_correct = Question._meta.get_field_by_name('answer_correct')[0]
        self.assertEquals(answer_correct.__class__, models.ForeignKey)
        self.assertFalse(answer_correct.blank)
        self.assertFalse(answer_correct.null)

    def test_lesson_field(self):
        lesson = Question._meta.get_field_by_name('lesson')[0]
        self.assertEquals(lesson.__class__, models.ForeignKey)
        self.assertFalse(lesson.blank)
        self.assertFalse(lesson.null)

    def test_audio_field(self):
        audio = Question._meta.get_field_by_name('audio')[0]
        self.assertEquals(audio.__class__, models.ForeignKey)
        self.assertTrue(audio.blank)
        self.assertTrue(audio.null)

    def test_image_field(self):
        image = Question._meta.get_field_by_name('image')[0]
        self.assertEquals(image.__class__, models.ForeignKey)
        self.assertTrue(image.blank)
        self.assertTrue(image.null)

class ResultModelTest(TestCase):
    # correct = models.IntegerField(verbose_name='Respostas corretas')
    # wrong = models.IntegerField(verbose_name='Respostas erradas')

    def test_user_field(self):
        user = Result._meta.get_field_by_name('user')[0]
        self.assertEquals(user.__class__, models.ForeignKey)
        self.assertFalse(user.blank)
        self.assertFalse(user.null)

    def test_lesson_field(self):
        lesson = Result._meta.get_field_by_name('lesson')[0]
        self.assertEquals(lesson.__class__, models.ForeignKey)
        self.assertFalse(lesson.blank)
        self.assertFalse(lesson.null)

    def test_finished_at_field(self):
        finished_at = Result._meta.get_field_by_name('finished_at')[0]
        self.assertEquals(finished_at.__class__, models.DateTimeField)

    def test_correct_field(self):
        correct = Result._meta.get_field_by_name('correct')[0]
        self.assertEquals(correct.__class__, models.IntegerField)
        self.assertFalse(correct.blank)
        self.assertFalse(correct.null)

    def test_wrong_field(self):
        wrong = Result._meta.get_field_by_name('wrong')[0]
        self.assertEquals(wrong.__class__, models.IntegerField)
        self.assertFalse(wrong.blank)
        self.assertFalse(wrong.null)

# encoding: utf-8
__author__ = 'jesuejunior'
from django.forms import TextInput, ModelForm, ChoiceField

from quiz.models import Question


class QuestionForm(ModelForm):
    answer = ChoiceField(widget=TextInput(attrs={
        'placeholder': 'Marque a resposta correta.',
    }))

    class Meta:
        model = Question

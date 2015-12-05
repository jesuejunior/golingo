from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse
from django.views.generic import View
from quiz.models import Question


class HomeTemplateView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        cxt = self.get_context_data()
        return TemplateResponse(
            request=self.request,
            template=self.template_name,
            context=cxt,
            **kwargs
        )

    def get_context_data(self, **kwargs):
        cxt = {}
        return cxt


class QuestionTemplateView(View):
    template_name = 'question.html'

    def get(self, request, *args, **kwargs):
        cxt = self.get_context_data()
        return TemplateResponse(
            request=self.request,
            template=self.template_name,
            context=cxt,
            **kwargs
        )

    def get_context_data(self, **kwargs):
        cxt = {}
        cxt['form_answers'] = Question.answers
        return cxt

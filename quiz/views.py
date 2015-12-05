# Create your views here.
from django.template.response import TemplateResponse
from django.views.generic import View, ListView
from quiz.models import Question, Unity


class HomeTemplateView(ListView):
    template_name = 'home.html'
    model = Unity

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        return context


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

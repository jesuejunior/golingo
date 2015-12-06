# Create your views here.
from django.template.response import TemplateResponse
from django.views.generic import View, ListView
from braces.views import LoginRequiredMixin
from quiz.models import Question, Unity, Lesson


class HomeTemplateView(ListView, LoginRequiredMixin):
    template_name = 'home.html'
    model = Unity

    def get_context_data(self, **kwargs):
        context = super(HomeTemplateView, self).get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.all()
        return context


class QuestionTemplateView(View):
    template_name = 'question.html'
    model = Question

    def get(self, request, *args, **kwargs):
        cxt = self.get_context_data()
        return TemplateResponse(
            request=self.request,
            template=self.template_name,
            context=cxt,
            **kwargs
        )

    def post(self, request, *args, **kwargs):
        cxt = self.get_context_data()
        req = request.POST
        authenticated = request.user.is_authenticated()
        if authenticated:
            req = req.copy()
            req[u'user'] = request.user.pk

        return TemplateResponse(
            request=self.request,
            template=self.template_name,
            context=cxt,
            **kwargs)

    def get_context_data(self, **kwargs):
        question = Question.objects.prefetch_related().all()[:1][0]
        cxt = {}
        cxt['question'] = question.name
        cxt['answers'] = question.answers.all
        return cxt
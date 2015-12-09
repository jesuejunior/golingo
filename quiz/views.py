# Create your views here.
from django.template.response import TemplateResponse
from django.views.generic import View, ListView
from braces.views import LoginRequiredMixin
from quiz.models import Question, Unity, Result


class HomeTemplateView(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    model = Unity


class QuestionTemplateView(LoginRequiredMixin, View):
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
        cxt = {
            'question': question.name,
            'answers': question.answers.all
        }

        return cxt


class ResultTemplateView(LoginRequiredMixin, View):
    template_name = 'results.html'
    model = Result

    def get(self, request, *args, **kwargs):
        lesson_id = kwargs.pop('lesson_id')
        cxt = self.get_context_data(request, lesson_id)
        return TemplateResponse(
            request=self.request,
            template=self.template_name,
            context=cxt,
            **kwargs
        )

    def get_context_data(self, request, lesson_id):
        user = request.user
        result = self.model.objects.filter(user_id=user.id, lesson_id=lesson_id).latest('finished_at')
        return {'results': [result], 'lesson': result.lesson}

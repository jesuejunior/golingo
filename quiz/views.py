# Create your views here.
from django.db.models import F
from django.template.response import TemplateResponse
from django.views.generic import View, ListView
from braces.views import LoginRequiredMixin
from quiz.models import Question, Unity, Result


class HomeTemplateView(LoginRequiredMixin, ListView):
    template_name = 'home.html'
    model = Unity


class QuestionTemplateView(LoginRequiredMixin, View):
    template_name = 'question.html'

    def get(self, request, *args, **kwargs):
        lesson_id = args[0]
        question_id = args[1]
        cxt = self.get_context_data(request, lesson_id, question_id)
        return TemplateResponse(
            request=self.request,
            template=self.template_name,
            context=cxt,
            **kwargs
        )

    def post(self, request, *args, **kwargs):
        lesson_id = args[0]
        question_id = args[1]
        cxt = self.get_context_data(request, lesson_id, question_id)
        req = request.POST
        authenticated = request.user.is_authenticated()
        answer = req.get('answer')
        if authenticated and answer:
            user_id = request.user.pk
            result = Result.objects.get_or_create(user=user_id, lesson=lesson_id)
            if self.question.answer_correct.id == int(answer[0]):
                result[0].correct = F('correct') + 1
            else:
                result[0].wrong = F('wrong') + 1
            result[0].save()

        return TemplateResponse(
            request=self.request,
            template=self.template_name,
            context=cxt,
            **kwargs)

    def get_context_data(self, request, lesson_id, question_id):
        self.question = Question.objects.prefetch_related().filter(lesson__id=lesson_id)[0]
        cxt = {
            'question': self.question,
            'answers': self.question.answers.all
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

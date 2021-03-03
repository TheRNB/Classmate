# from django.shortcuts import render
# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
# from django.views.generic import TemplateView
from homework.models import Answer


class ProfessorHomework(View):
    template_name = 'professor_homework.html'

    def get(self, request):
        answer = Answer.objects.all()
        return render(request, self.template_name, context={'document': answer.answer_document,
                                                            'scores': answer.score,
                                                            'ids': answer.student_id})

    def post(self, request):
        pass


class StudentHomework(View):
    template_name = 'student_homework.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass

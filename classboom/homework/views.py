# from django.shortcuts import render
# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
# from django.views.generic import TemplateView
from homework.models import Answer, Question


class ProfessorHomework(View):
    template_name = 'professor_homework.html'

    def get(self, request):
        question = Question.objects.all()
        return render(request, self.template_name, context={"question": question})


class ProfessorHomeworkSpecificAnswer(View):
    def get(self, request, id):
        answer = Question.objects.get(id=id)
        return render(request, 'professor_homework_answer.html', context={"answer": answer})


class StudentHomework(View):
    def get(self, request):
        question = Question.objects.all()
        current_user = request.user
        return render(request, 'student_homework.html', context={"question": question, "current_user": current_user})

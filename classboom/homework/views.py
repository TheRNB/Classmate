# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
# from django.views.generic import TemplateView
from .models import Answer, Question
from .form import HomeworkCreationForm


class ProfessorHomework(View):
    template_name = 'professor_homework.html'

    def get(self, request):
        question = Question.objects.all()
        return render(request, self.template_name, context={"question": question})

    def post(self, request):
        form = HomeworkCreationForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["question_title"]
            deadline = form.cleaned_data["deadline_date"]
            info = form.cleaned_data["explanation"]
            document = form.cleaned_data["document"]
            new_homework = Question(question_title=title, deadline_date=deadline, explanation=info, document=document)
            new_homework.save()
            return redirect("professor_homework")
        else:
            return redirect("professor_homework_creation")

class ProfessorHomeworkCreation(View):
    template_name = 'professor_homework_creation.html'

    def get(self, request):
        form = HomeworkCreationForm()
        return render(request, self.template_name, context={"form": form})

    def post(self, request):
        form = HomeworkCreationForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["question_title"]
            deadline = form.cleaned_data["deadline_date"]
            info = form.cleaned_data["explanation"]
            document = form.cleaned_data["document"]
            new_homework = Question(question_title=title, deadline_date=deadline, explanation=info, document=document)
            new_homework.save()
            return redirect("professor_homework")
        else:
            return redirect("professor_homework_creation")


class ProfessorHomeworkSpecificAnswer(View):
    template_name = 'professor_homework_answer.html'

    def get(self, request, id):
        answer = Question.objects.get(id=id)
        return render(request, self.template_name, context={"answer": answer})


class StudentHomework(View):
    template_name = 'student_homework.html'

    def get(self, request):
        question = Question.objects.all()
        return render(request, self.template_name, context={"question": question})

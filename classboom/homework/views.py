# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
# from django.views.generic import TemplateView
from .models import Answer, Question
from .form import HomeworkCreationForm, HomeworkUploadForm


class ProfessorHomework(View):
    template_name = 'professor_homework.html'

    def get(self, request):
        question = Question.objects.all()
        return render(request, self.template_name, context={"question": question})


class ProfessorHomeworkCreation(View):
    template_name = 'professor_homework_creation.html'

    def get(self, request):
        form = HomeworkCreationForm()
        return render(request, self.template_name, context={"form": form})

    def post(self, request):
        form = HomeworkCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("professor_homework")
        else:
            form = HomeworkCreationForm()
            return render(request, self.template_name, context={"form": form})


class ProfessorHomeworkSpecificAnswer(View):
    template_name = 'professor_homework_answer.html'

    def get(self, request, id):
        answer = Question.objects.get(id=id)
        return render(request, self.template_name, context={"answer": answer})

    def post(self, request, id):
        ans = Question.objects.get(id=id)
        for answers in ans.answer_set.all():
            if (request.POST.get("newScore" + str(answers.id)) and
                    100 >= int(request.POST.get("newScore" + str(answers.id))) >= 0):
                answers.score = request.POST.get("newScore" + str(answers.id))
                answers.save()
        return redirect("professor_homework_answer", id)


class StudentHomework(ProfessorHomework):
    template_name = 'student_homework.html'


class StudentHomeworkCreation(View):
    template_name = 'student_homework_creation.html'
    current_id = 0

    def get(self, request, id):
        form = HomeworkUploadForm()
        self.current_id = id
        explanation = Question.objects.get(id=id)
        return render(request, self.template_name, context={"form": form, "explanation": explanation.explanation})

    def post(self, request, id):
        form = HomeworkUploadForm(request.POST, request.FILES)
        self.current_id = id
        if form.is_valid():
            ans = Answer(form, question=Question.objects.get(id=self.current_id))
            # form.save()
            ans.save()
            return redirect("student_homework")
        else:
            form = HomeworkUploadForm()
            explanation = Question.objects.get(id=id).explanation
            return render(request, self.template_name, context={"form": form, "explanation": explanation})

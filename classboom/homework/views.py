# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime
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
        print(form.is_valid())
        if form.is_valid():
            que = Question(question_title=form.cleaned_data["question_title"],
                           explanation=form.cleaned_data["explanation"], document=form.cleaned_data["document"],
                           deadline_date=request.POST.get("deadline_date"))
            que.save()
            return redirect("professor_homework")
        else:
            form = HomeworkCreationForm()
            # return render(request, self.template_name, context={"form": form})
            return HttpResponse("You done goofed")


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

    def get(self, request):
        answers = []
        questions = []
        current_time = datetime.now()
        for quest in Question.objects.all():
            print("$$$$", quest.deadline_date)
            if quest.answer_set.all():
                answer = quest.answer_set.get(user=request.user)
                if answer:
                    answers.append(answer)
                else:
                    questions.append(quest)
            else:
                questions.append(quest)
        print("####", current_time)
        return render(request, self.template_name, context={"question": questions, "answer": answers,
                                                            "current_time": current_time})


class StudentHomeworkCreation(View):
    template_name = 'student_homework_creation.html'

    def get(self, request, id):
        form = HomeworkUploadForm()
        explanation = Question.objects.get(id=id)
        return render(request, self.template_name, context={"form": form, "explanation": explanation.explanation})

    def post(self, request, id):
        form = HomeworkUploadForm(request.POST, request.FILES)
        if form.is_valid():
            question = Question.objects.get(id=id)
            answer = question.answer_set.get(user=request.user)
            if answer:
                answer.answer_document = form.cleaned_data['answer_document']
                answer.upload_date = datetime.now()
            else:
                answer = question.answer_set.create(user=request.user)
                answer.answer_document = form.cleaned_data['answer_document']

            answer.save()
            return redirect("student_homework")

        else:
            form = HomeworkUploadForm()
            explanation = Question.objects.get(id=id).explanation
            return render(request, self.template_name, context={"form": form, "explanation": explanation})

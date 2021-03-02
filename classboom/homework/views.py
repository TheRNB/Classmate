from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View


class ProfessorHomework(View):
    template_name = 'professor_homework.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass


class StudentHomework(View):
    template_name = 'student_homework.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        pass

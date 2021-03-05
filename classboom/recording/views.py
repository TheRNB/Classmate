# from django.shortcuts import render
# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .models import Recording
# from django.views.generic import TemplateView
from homework.models import Answer


class ProfessorRecording(View):
    template_name = 'professor_recording.html'

    def get(self, request):
        videos = Recording.objects.all()
        return render(request, self.template_name, context={"videos": videos})


class StudentRecording(View):
    template_name = 'student_recording.html'

    def get(self, request):
        videos = Recording.objects.all()
        return render(request, self.template_name, context={"videos": videos})


class StudentSpecificRecording(View):
    template_name = 'student_recording_specific.html'

    def get(self, request, id):
        videos = Recording.objects.get(id=id)
        pass

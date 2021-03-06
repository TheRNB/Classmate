# from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
# from django.views.generic import TemplateView
from homework.models import Answer
from .models import Recording
from .form import RecordingCreationForm


class ProfessorRecording(View):
    template_name = 'professor_recording.html'

    def get(self, request):
        recording = Recording.objects.all()
        return render(request, self.template_name, context={"videos": recording})

    def post(self, request):
        form = RecordingCreationForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            video = form.cleaned_data["video"]
            new_video = Recording(title=title, video=video)
            new_video.save()
            return HttpResponseRedirect("/rec/prf")
        else:
            return HttpResponseRedirect("/rec/prf/prc")


class ProfessorRecordingCreation(View):
    template_name = 'professor_recording_creation.html'

    def get(self, request):
        form = RecordingCreationForm()
        return render(request, self.template_name, context={"form": form})

    def post(self, request):
        form = RecordingCreationForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            video = form.cleaned_data["video"]
            new_video = Recording(title=title, video=video)
            new_video.save()
            return HttpResponseRedirect("/rec/prf")
        else:
            return HttpResponseRedirect("/rec/prf/prc")


class StudentRecording(View):
    template_name = 'student_recording.html'

    def get(self, request):
        recording = Recording.objects.all()
        return render(request, self.template_name, context={"videos": recording})

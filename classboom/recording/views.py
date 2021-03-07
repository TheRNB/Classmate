# from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
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


class ProfessorRecordingCreation(View):
    template_name = 'professor_recording_creation.html'

    def get(self, request):
        form = RecordingCreationForm()
        return render(request, self.template_name, context={"form": form})

    def post(self, request):
        form = RecordingCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("professor_recording")
        else:
            form = RecordingCreationForm()
            return render(request, self.template_name, context={"form": form})


class ProfessorRecordingStream(View):
    template_name = 'professor_recording_stream.html'

    def get(self, request, id):
        video = Recording.objects.get(id=id)
        return render(request, self.template_name, context={"vid": video})


class StudentRecording(ProfessorRecording):
    template_name = 'student_recording.html'


class StudentRecordingStream(ProfessorRecordingStream):
    template_name = 'student_recording_stream.html'

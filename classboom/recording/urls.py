from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import *


urlpatterns = [
    # Student homework page
    path('stu/', StudentRecording.as_view(), name="student_recording"),
    # Professor homework page
    path('prf/prc/', ProfessorRecordingCreation.as_view(), name="professor_recording_creation"),
    path('prf/', ProfessorRecording.as_view(), name="professor_recording"),
]

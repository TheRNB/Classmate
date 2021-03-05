from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import ProfessorRecording, StudentRecording, StudentSpecificRecording


urlpatterns = [
    # Student homework page
    path('stu/', StudentRecording.as_view()),
    path('stu/<int:id>', StudentSpecificRecording.as_view()),
    # Professor homework page
    path('prf/', ProfessorRecording.as_view()),
]

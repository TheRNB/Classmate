from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import *


urlpatterns = [
    # Student homework page
    path('stu/', StudentHomework.as_view(), name="student_homework"),
    # Professor homework page
    path('prf/<int:id>', ProfessorHomeworkSpecificAnswer.as_view()),
    path('prf/hwc', ProfessorHomeworkCreation.as_view(), name="professor_homework_creation"),
    path('prf/', ProfessorHomework.as_view(), name="professor_homework"),
]

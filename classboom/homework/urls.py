from django.urls import path, include
from django.views.generic.base import TemplateView
from .views import ProfessorHomework, ProfessorHomeworkSpecificAnswer, StudentHomework


urlpatterns = [
    # Student homework page
    path('stu/', StudentHomework.as_view()),
    # Professor homework page
    path('prf/', ProfessorHomework.as_view()),
    path('prf/<int:id>', ProfessorHomeworkSpecificAnswer.as_view()),
]

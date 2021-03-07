from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    # Student homework page
    path('stu/<int:id>', StudentHomeworkCreation.as_view(), name="student_homework_upload"),
    path('stu/', StudentHomework.as_view(), name="student_homework"),
    # Professor homework page
    path('prf/<int:id>', ProfessorHomeworkSpecificAnswer.as_view()),
    path('prf/hwc', ProfessorHomeworkCreation.as_view(), name="professor_homework_creation"),
    path('prf/', ProfessorHomework.as_view(), name="professor_homework"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

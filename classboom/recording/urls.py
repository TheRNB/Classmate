from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    # Student homework page
    path('stu/<int:id>', StudentRecordingStream.as_view(), name="student_recording_stream"),
    path('stu/', StudentRecording.as_view(), name="student_recording"),
    # Professor homework page
    path('prf/prc/', ProfessorRecordingCreation.as_view(), name="professor_recording_creation"),
    path('prf/<int:id>', ProfessorRecordingStream.as_view(), name="professor_recording_stream"),
    path('prf/', ProfessorRecording.as_view(), name="professor_recording"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

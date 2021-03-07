from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('', LoginVi.as_view()),
    path('register/', RegisterView.as_view(), name="reg")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

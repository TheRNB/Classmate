from django.forms import ModelForm
from .models import Recording


class RecordingCreationForm(ModelForm):
    class Meta:
        model = Recording
        fields = ['title', 'video']

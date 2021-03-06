from django import forms

from .validators import validate_video_file_extension


class RecordingCreationForm(forms.Form):
    title = forms.CharField(max_length=200)
    pub_date = forms.DateTimeField()
    video = forms.FileField(validators=[validate_video_file_extension])

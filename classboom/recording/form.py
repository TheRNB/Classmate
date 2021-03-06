from django import forms

from .validators import validate_video_file_extension


class RecordingCreationForm(forms.Form):
    title = forms.CharField(max_length=200, label="عنوان")
    video = forms.FileField(label="ویدئو", validators=[validate_video_file_extension])

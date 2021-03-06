from django import forms

from .validators import validate_document_file_extension, validate_score


class HomeworkCreationForm(forms.Form):
    question_title = forms.CharField(max_length=256, label="نام سوال")
    deadline_date = forms.DateTimeField(label="ددلاین")
    explanation = forms.CharField(max_length=512, label="توضیحات")
    document = forms.FileField(validators=[validate_document_file_extension], label="فایل ارسالی")

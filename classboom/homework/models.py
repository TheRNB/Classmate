from django.db import models
from authentication.models import CustomUser
from datetime import datetime

from .validators import validate_document_file_extension, validate_score


class Question(models.Model):
    question_title = models.CharField(max_length=256)
    pub_date = models.DateTimeField(default=datetime.now)
    deadline_date = models.DateTimeField(default=datetime.now)
    explanation = models.CharField(max_length=512, default="")
    document = models.FileField(upload_to="questions", validators=[validate_document_file_extension])


class Answer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="answer_id", null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_document = models.FileField(upload_to="answers", validators=[validate_document_file_extension])
    score = models.IntegerField(null=True, validators=[validate_score])
    upload_date = models.DateTimeField(default=datetime.now)

from django.db import models

from .validators import validate_document_file_extension, validate_score


class Question(models.Model):
    question_title = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')
    deadline_date = models.DateTimeField()
    explanation = models.CharField(max_length=512)
    document = models.FileField(upload_to="upload/%Y/%m/%d", validators=[validate_document_file_extension])


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_document = models.FileField(upload_to="upload/%Y/%m/%d", validators=[validate_document_file_extension])
    score = models.DecimalField(max_digits=4, decimal_places=2, validators=[validate_score])


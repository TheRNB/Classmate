from django.db import models

from .validators import validate_video_file_extension


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    deadline_date = models.DateTimeField()
    # FileField.storage() to call the file
    # video.url to see the URL
    video = models.FileField(upload_to='uploads/%Y/%m/%d/', validators=[validate_video_file_extension])


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


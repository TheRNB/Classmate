from django.forms import ModelForm
from .models import Question, Answer


class HomeworkCreationForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_title', 'deadline_date', 'explanation', 'document', ]


class HomeworkUploadForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_document']


class HomeworkScoreForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['id', 'score', ]

import os
from django.core.exceptions import ValidationError


def validate_document_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx', '.xls']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


def validate_score(value):
    if value > 20 or value < 0:
        raise ValidationError('The scores should be from 0 to 20.')
from django.db import models


class AuthenticationIds:
    id = models.IntegerField(default=-1)
    email_address = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

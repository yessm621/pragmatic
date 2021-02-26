from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    image = models.CharField(max_length=200, null=False)
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now=True)

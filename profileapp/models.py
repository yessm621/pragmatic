from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')
    image = models.CharField(max_length=255, null=True)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)

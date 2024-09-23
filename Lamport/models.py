from django.db import models

from django.db import models


class UserPass(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)  # Store the hashed password
    n = models.IntegerField()

    def __str__(self):
        return self.username

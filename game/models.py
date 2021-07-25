from django.db import models
from django.contrib.auth.models import User


class GameAccount(models.Model):
    # will hold a One-To-One relationship with the existing User Model
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    credit = models.IntegerField(default=10000)
    level = models.IntegerField(default=1, blank=True)

    def __str__(self):
        return str(self.user)
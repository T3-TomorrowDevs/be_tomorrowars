from django.db import models
from django.contrib.auth.models import User

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserAccount(models.Model):
    """
    Create a table UserAccount to store the googleid related to userid and create the token
    to send after the login/signup
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    google_id = models.CharField(max_length=100)

    # automatically generates the token for each user
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=user, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)

    def __str__(self):
        return str(self.user)

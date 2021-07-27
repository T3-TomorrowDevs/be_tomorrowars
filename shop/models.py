from django.db import models

class Troop(models.Model):
    troop_id = models.IntegerField(default = 0)

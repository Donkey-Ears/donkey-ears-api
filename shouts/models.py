from django.db import models
from core.models import TimeStampedModel


class Shout(TimeStampedModel):
    user = models.ForeignKey(
        "users.User", related_name="shouts", on_delete=models.CASCADE
    )
    text = models.TextField(max_length=200)

from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User Model
    """

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_THIRD = "third"
    GENDER_CHOICES = (
        (GENDER_MALE, "남성"),
        (GENDER_FEMALE, "여성"),
        (GENDER_THIRD, "그 밖"),
    )

    AGE_TEEN = "10s"
    AGE_TWENTIES = "20s"
    AGE_THIRTYS = "30s"
    AGE_FOURTYS = "40s"
    AGE_CHOICES = (
        (AGE_TEEN, "10대"),
        (AGE_TWENTIES, "20대"),
        (AGE_THIRTYS, "30대"),
        (AGE_FOURTYS, "40대"),
    )

    gender = models.CharField(choices=GENDER_CHOICES, max_length=8, blank=False)
    age = models.CharField(choices=AGE_CHOICES, max_length=5, blank=False)

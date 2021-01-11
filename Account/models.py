from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
gender_choices = (
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others')
)
class custom_user_model(AbstractUser):
    email = models.CharField(max_length=50)
    gender = models.CharField(max_length=20,choices=gender_choices)
    contact_no = models.CharField(max_length=12)
    address = models.CharField(max_length=50)
    def __str__(self):
        return self.username
    
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)


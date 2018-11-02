from django.db import models

class Member(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    pw = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

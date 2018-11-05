from django.db import models

class Member(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    pw = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

class boardDb(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    write_time = models.DateTimeField(auto_now_add=True)
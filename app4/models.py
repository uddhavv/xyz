from django.db import models

class Uvg(models.Model):
    dname=models.CharField(max_length=25)
    dadd=models.CharField(max_length=25)
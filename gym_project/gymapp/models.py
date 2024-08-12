from django.db import models

# Create your models here.

class Gym(models.Model):
    name=models.CharField(max_length=30)
    plan=models.CharField(max_length=30)
    price=models.IntegerField()
    training=models.CharField(max_length=30, default='default_value')

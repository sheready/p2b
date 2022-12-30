from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    cost = models.DecimalField(max_digits=6, decimal_places=2)


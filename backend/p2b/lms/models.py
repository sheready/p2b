from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.CharField(max_length=100, blank=True, default='')
    cost = models.FloatField()
    photo = models.ImageField(blank=True, null=True, default=None, upload_to='uploads/images')
    video = models.FileField(upload_to='uploads/videos',null=True,validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])


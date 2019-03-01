from django.db import models
from datetime import date
from datetime import datetime


# Create your models here.
class TeacherModel(models.Model):
    name = models.CharField(max_length=50, default='')
    school = models.CharField(max_length=50, default='')
    subject = models.CharField(max_length=50, default='')
    hours = models.DecimalField(max_digits=3, decimal_places=2)
    workDate = models.DateField(default=date.today())
    entryDate = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name

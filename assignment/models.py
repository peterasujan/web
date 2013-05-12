from django.db import models
from datetime import date

# Create your models here.

class Assignment(models.Model):
    name = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    date = models.DateField(default=date(year=1970, month=1, day=1))

    def __unicode__(self):
        return self.name

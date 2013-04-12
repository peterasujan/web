from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlobField(models.Field):
    description = "Blob"
    def db_type(self):
        return 'blob'

class Verb(models.Model):
    verb = models.CharField(max_length=30)

class ActivityLog(models.Model):
    subject = models.ForeignKey(User)
    verb = models.ForeignKey(Verb)
    object = BlobField()


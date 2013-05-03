from django.db import models
from django.contrib.auth.models import User

class BlobField(models.Field):
    description = "Blob"
    def db_type(self, connection):
        return 'blob'

class Verb(models.Model):
    verb = models.CharField(max_length=30)

class ActivityLog(models.Model):
    subject = models.CharField(max_length=36)
    verb = models.ForeignKey(Verb)
    object = BlobField()
    time = models.DateTimeField()


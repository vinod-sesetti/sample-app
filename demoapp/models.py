from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=1000, unique=True)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title

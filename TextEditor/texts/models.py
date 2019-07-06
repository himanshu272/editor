from django.db import models

# Create your models here.


class Notes(models.Model):
    notes = models.TextField()
    username = models.CharField(max_length=32)
    language = models.CharField(max_length=16)
    filename = models.CharField(max_length=32, default="test")

    def __str__(self):
        return self.username

from django.db import models

# Create your models here.


class MyInfo(models.Model):
    slackUsername = models.CharField(max_length=50)
    backend = models.BooleanField()
    age = models.IntegerField()
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.slackUsername

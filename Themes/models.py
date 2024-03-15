from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)
    view = models.CharField(max_length=100)
    template = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.name

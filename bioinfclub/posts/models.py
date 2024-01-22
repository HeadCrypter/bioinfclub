from django.db import models

class Post(models.Model):
    abstract = models.CharField(max_length=256)
    description = models.CharField(max_length=2500)
    date = models.DateField()
    picture = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=256, blank=True)


    def __str__(self):
        return self.abstract
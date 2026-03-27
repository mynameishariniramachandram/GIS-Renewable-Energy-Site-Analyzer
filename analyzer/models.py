from django.db import models

class District(models.Model):

    name = models.CharField(max_length=100)

    lat = models.FloatField()
    lon = models.FloatField()

    solar = models.FloatField()
    wind = models.FloatField()

    score = models.FloatField()

    def __str__(self):
        return self.name
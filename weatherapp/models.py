from django.db import models

# Create your models here.

class weatherreport(models.Model):
    city = models.CharField(max_length=50)
    condition = models.CharField(max_length=100)
    temperature = models.IntegerField()
    date = models.DateField()

    def __unicode__(self):
        return self.city



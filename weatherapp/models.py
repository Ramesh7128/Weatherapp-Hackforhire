from django.db import models

# Create your models here.

class weatherreport(models.Model):
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    date = models.CharField(max_length=30)
    condition = models.CharField(max_length=100)
    temperature = models.IntegerField()
    date = models.DateField()

    def __unicode__(self):
        return self.state



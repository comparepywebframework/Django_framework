from django.db import models


class Shop(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    street_number = models.IntegerField()
    open_at = models.TimeField()
    close_at = models.TimeField()

def __str__(self):
    return self.name
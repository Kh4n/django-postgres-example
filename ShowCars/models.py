from django.db import models
from django.db.models.query import QuerySet

# Create your models here.


class Car(models.Model):
    make = models.CharField(max_length=70, blank=False, default='')
    model = models.CharField(max_length=70, blank=False, default='')
    year = models.IntegerField()


def car_qs_to_json(qs: QuerySet):
    data = []
    for car in qs:
        data.append([car.make, car.model, car.year])
    return {"data": data}

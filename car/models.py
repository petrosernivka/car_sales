from django.db import models


class Car(models.Model):
    class Meta():
        db_table = 'car'

    car_brand = models.CharField(max_length = 30)
    car_model = models.CharField(max_length = 30)

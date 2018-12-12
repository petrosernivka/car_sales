from django.db import models


class Car(models.Model):
    class Meta():
        db_table = 'car'

    car_brand = models.CharField(max_length = 20)
    car_model = models.CharField(max_length = 20)

from django.db import models


class CarBrand(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Advert(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(CarModel, on_delete=models.SET_NULL, null=True)
    category = models.IntegerField()
    price = models.IntegerField()
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

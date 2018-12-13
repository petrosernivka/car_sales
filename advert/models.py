from django.db import models

class Advert(models.Model):
    class Meta():
        db_table = 'advert'

    advert_brand = models.CharField(max_length = 30)
    advert_model = models.CharField(max_length = 30)
    advert_category = models.CharField(max_length = 30)
    advert_price = models.IntegerField()
    advert_owner = models.CharField(max_length = 50)

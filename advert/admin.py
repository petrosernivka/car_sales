from django.contrib import admin
from .models import Advert, CarBrand, CarModel


class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Advert, AuthorAdmin)
admin.site.register(CarBrand, AuthorAdmin)
admin.site.register(CarModel, AuthorAdmin)

from django import forms
from .models import Advert, CarModel

class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ('brand', 'model', 'category', 'price', 'name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model'].queryset = CarModel.objects.none()

        if 'brand' in self.data:
            try:
                brand_id = int(self.data.get('brand'))
                self.fields['model'].queryset = CarModel.objects.filter(brand_id=brand_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the advert; ignore and fallback to empty CarModel queryset
        elif self.instance.pk:
            self.fields['model'].queryset = self.instance.brand.carmodel_set.order_by('name')

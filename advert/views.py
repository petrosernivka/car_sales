from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Advert, CarModel
from .forms import AdvertForm


class AdvertListView(ListView):
    model = Advert
    context_object_name = 'adverts'


class AdvertCreateView(CreateView):
    model = Advert
    form_class = AdvertForm
    success_url = reverse_lazy('advert_changelist')


class AdvertUpdateView(UpdateView):
    model = Advert
    form_class = AdvertForm
    success_url = reverse_lazy('advert_changelist')


def load_models(request):
    brand_id = request.GET.get('brand')
    models = CarModel.objects.filter(brand_id=brand_id).order_by('name')
    return render(request, 'advert/model_dropdown_list_options.html', {'models': models})

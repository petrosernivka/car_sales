from django.urls import include, path
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.AdvertListView.as_view(), name='advert_changelist'),
    path('add/', views.AdvertCreateView.as_view(), name='advert_add'),
    path('<int:pk>/', views.AdvertUpdateView.as_view(), name='advert_change'),
    path('ajax/load-models/', views.load_models, name='ajax_load_models'),
]

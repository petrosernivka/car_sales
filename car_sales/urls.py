from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='advert_changelist'), name='home'),
    path('admin/', admin.site.urls),
    path('advert/', include('advert.urls')),
]

from catalog.apps import CatalogConfig
from django.urls import path

from catalog.views import contacts, home

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contacts, name='contacts'),
    path('', home, name='home'),

]

from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^record$', views.NavigationApi),
    url(r'^record/([0-9]+)$', views.NavigationApi),
    url(r'^vehicle$', views.VehicleApi),
    url(r'^vehicle/([0-9]+)$', views.VehicleApi),
]
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.bid_field, name='bid_field'),
]
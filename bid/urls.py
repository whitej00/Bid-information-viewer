from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.moniter_field, name='moniter_field'),
    path('bid_field/', views.bid_field, name='bid_field'),
    path('bid_dtfield/<str:idk>', views.bid_dtfield, name='bid_dtfield'),
]
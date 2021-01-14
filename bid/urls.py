from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.moniter_field, name='moniter_field'),
    path('search_field/', views.search_field, name='search_field'),
    path('detail_field/<str:idk>', views.detail_field, name='detail_field'),
]
from django.urls import path
from . import views



urlpatterns = [
    path('', views.AppOrder.as_view(), name='order_view'),
]
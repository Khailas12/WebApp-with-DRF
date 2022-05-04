from django.urls import path
from . import views



urlpatterns = [
    # path('', views.AppOrder.as_view(), name='order_view'),
    path('', views.AppOrderCreate.as_view()),
    path('order/', views.AppOrderDetail.as_view()),
]
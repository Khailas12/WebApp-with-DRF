from django.urls import path
from . import views


urlpatterns = [
    path('', views.Auth.as_view(), name='auth'),
    path('signup/', views.UserView.as_view())
]

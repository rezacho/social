from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RgisterView.as_view(), name='user_register')
]

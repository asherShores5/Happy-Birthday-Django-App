from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.your_view, name='your_view'),
]

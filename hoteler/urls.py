from django.urls import path
from .views import hotel_list_create

urlpatterns = [
    path('hotels/', hotel_list_create, name='hotel-list-create'),
]

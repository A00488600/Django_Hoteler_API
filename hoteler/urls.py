from django.urls import path
from .views import get_list_of_hotels, reservation_confirmation

urlpatterns = [
    path('hotels/', get_list_of_hotels, name='getListOfHotels'),
    path('reserve/', reservation_confirmation, name='reservationConfirmation'),
]

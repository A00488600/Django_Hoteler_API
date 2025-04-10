from rest_framework import serializers
from .models import Hotel, Guest, Reservation


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['name', 'price', 'availability']


class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = ['guest_name', 'gender']


class ReservationSerializer(serializers.ModelSerializer):
    guests_list = GuestSerializer(many=True, write_only=True)
    confirmation_number = serializers.CharField(read_only=True)

    class Meta:
        model = Reservation
        fields = ['hotel_name', 'checkin', 'checkout',
                  'guests_list', 'confirmation_number']

    def create(self, validated_data):
        guests_data = validated_data.pop('guests_list')
        reservation = Reservation.objects.create(**validated_data)
        for guest in guests_data:
            g = Guest.objects.create(**guest)
            reservation.guests.add(g)
        return reservation

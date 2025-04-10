from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hotel
from .serializers import HotelSerializer, ReservationSerializer


@api_view(['GET'])
def get_list_of_hotels(request):
    hotels = Hotel.objects.all()
    serializer = HotelSerializer(hotels, many=True)
    return Response({'hotels_list': serializer.data})


@api_view(['POST'])
def reservation_confirmation(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        reservation = serializer.save()
        return Response({'confirmation_number': reservation.confirmation_number})
    return Response(serializer.errors, status=400)

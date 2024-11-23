from rest_framework import generics
from .models import Reservation
from .serializers import ReservationSerializer

# ADMIN - Create Reservation for Player
class ReservationListCreateView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# ADMIN - View Reservations of Players
class ReservationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView
from .serializers import RegisterSerializer, CreateGymSerializer, CreateClassSerializer, ClassSerializer, \
    BookClassSerializer, BookingSerializer, GymSerializer
from .models import Gym, Class, Booking
from .permissions import IsCancelable


class Register(CreateAPIView):
    serializer_class = RegisterSerializer


class CreateGym(CreateAPIView):
    serializer_class = CreateGymSerializer


class GymList(ListAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer


class CreateClass(CreateAPIView):
    serializer_class = CreateClassSerializer

    def perform_create(self, serializer):
        serializer.save(available=self.request.data["capacity"])


class ClassList(ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class BookClass(CreateAPIView):
    serializer_class = BookClassSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class Bookings(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class CancelBooking(DestroyAPIView):
    queryset = Booking.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'
    permission_classes = [IsCancelable]

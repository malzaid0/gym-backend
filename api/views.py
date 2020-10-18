from django.utils import timezone
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView
from .serializers import RegisterSerializer, CreateGymSerializer, CreateClassSerializer, ClassSerializer, \
    BookClassSerializer, BookingSerializer, GymSerializer
from .models import Gym, Class, Booking
from .permissions import IsCancelable, IsBookingOwner
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.core.mail import send_mail


class Register(CreateAPIView):
    serializer_class = RegisterSerializer


class CreateGym(CreateAPIView):
    serializer_class = CreateGymSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class GymList(ListAPIView):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer
    permission_classes = [IsAuthenticated]


class CreateClass(CreateAPIView):
    serializer_class = CreateClassSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(available=self.request.data["capacity"])


class ClassList(ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsAuthenticated]


class BookClass(CreateAPIView):
    serializer_class = BookClassSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        booked = Class.objects.get(id=int(self.request.data["gym_class"]))
        days_left = (booked.date - timezone.now().date()).days
        if days_left > 0:
            pass
        elif days_left == 0:
            if booked.time > timezone.now().time():
                pass
            else:
                raise ValidationError('Class is old')
        else:
            raise ValidationError('Class is old')
        if booked.available <= 0:
            raise ValidationError('Class is fully booked')
        else:
            booked.available -= 1
            booked.save()
        instance = serializer.save(user=self.request.user)
        send_mail(
            'Class booked',
            f"booking id: {instance.id}",
            '3a1a3f93e1-d2fae3@inbox.mailtrap.io',
            [self.request.user.email],
            fail_silently=False,)


class Bookings(ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated, ]


class CancelBooking(DestroyAPIView):
    queryset = Booking.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'
    permission_classes = [IsAuthenticated, IsCancelable, IsBookingOwner]

from django.db import models
from django.contrib.auth.models import User


class Gym(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Class(models.Model):
    CARDIO = 'CR'
    STRENGTH = 'ST'
    KICKBOXING = 'KB'
    SWIMMING = 'SW'
    CLASSES_TYPES = [('Cardio', 'Cardio'), ('Strength', 'Strength'), ('Kickboxing', 'Kickboxing'), ('Swimming', 'Swimming'), ]
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    type = models.CharField(max_length=15, choices=CLASSES_TYPES, default=CARDIO,)
    date = models.DateField()
    time = models.TimeField()
    is_free = models.BooleanField()
    capacity = models.PositiveSmallIntegerField()
    available = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.title} at {self.gym.name} gym"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookers")
    gym_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name="bookings")

    def __str__(self):
        return f"{self.user.first_name} booked {self.gym_class.title} at {self.gym_class.gym.name} gym"

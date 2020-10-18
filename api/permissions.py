from rest_framework.permissions import BasePermission
from django.utils import timezone


class IsBookingOwner(BasePermission):
    message = "You must be the owner of this booking"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.user == request.user):
            return True
        else:
            return False


class IsCancelable(BasePermission):
    message = "Booking cannot be cancelled or modified"

    def has_object_permission(self, request, view, obj):
        days_left = (obj.gym_class.date - timezone.now().date()).days
        if days_left > 0:
            return True
        elif days_left == 0:
            if obj.gym_class.time > timezone.now().time():
                return True
            else:
                return False
        else:
            return False

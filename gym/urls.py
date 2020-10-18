"""gym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('gyms/', views.GymList.as_view(), name="gym-list"),
    path('gyms/create/', views.CreateGym.as_view(), name="create-gym"),

    path('classes/', views.ClassList.as_view(), name="class-list"),
    path('classes/create/', views.CreateClass.as_view(), name="create-class"),

    path('bookings/', views.Bookings.as_view(), name="booking-list"),
    path('bookings/create/', views.BookClass.as_view(), name="book-class"),
    path('bookings/<int:booking_id>/cancel/', views.CancelBooking.as_view(), name="cancel-booking"),

    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
    path('register/', views.Register.as_view(), name="register"),
]
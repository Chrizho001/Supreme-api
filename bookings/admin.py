

# Register your models here.
# bookings/admin.py

from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(ModelAdmin):
    list_display = (
        "id",
        "name",
        "email",
        "quantity",
        "address",
        "created_at",
    )

    list_filter = ("created_at",)
    search_fields = ("name", "address")
    ordering = ("-created_at",)

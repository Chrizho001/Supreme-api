# bookings/models.py

from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or "Anonymous Booking"

    class Meta:
        ordering = ["-created_at"]

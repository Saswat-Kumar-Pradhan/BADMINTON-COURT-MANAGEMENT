from django.db import models

# Create your models here.

class Reservation(models.Model):
    court_no = models.IntegerField(help_text="Court number, must be a positive integer.")
    start_time = models.DateTimeField(help_text="The start time of the reservation.")
    duration = models.IntegerField(help_text="Duration of the reservation in hours.")
    name = models.CharField(max_length=100, help_text="Name of the person making the reservation.")
    phone = models.CharField(max_length=15, help_text="Phone number of the person making the reservation.")
    email = models.EmailField(help_text="Email address of the person making the reservation.")
    otp = models.CharField(max_length=6, help_text="One-time password for the reservation.")
    booking_status = models.BooleanField(default=False, help_text="Booking status, True if confirmed.")

    def __str__(self):
        return f"Reservation {self.id} for {self.name} at court {self.court_no}"

    class Meta:
        ordering = ['start_time']

class Announcement(models.Model):
    message = models.TextField(help_text="The content of the announcement.")
    date = models.DateField(help_text="The date of the announcement.")

    def __str__(self):
        return f"Announcement on {self.date}: {self.message[:50]}"

    class Meta:
        ordering = ['-date']
        verbose_name = "Announcement"
        verbose_name_plural = "Announcements"
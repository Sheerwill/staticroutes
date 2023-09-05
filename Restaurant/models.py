from django.db import models

# Create your models here.

class Booking(models.model):
    ID = models.BigIntegerField(primary_key=True, max_digits = 11)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(max_digits=6)
    Booking_date = models.DateTimeField()

class Menu(models.model):
    ID = models.BigIntegerField(primary_key=True, max_digits=5)
    Title = models.CharField(max_length=255)
    Price = models.FloatField(max_digits=10, decimal_places=2)
    Inventory = models.IntegerField(max_digits = 5)
    
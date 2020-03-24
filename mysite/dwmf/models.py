from django.db import models
from django.urls import reverse
from datetime import date, time, timezone, datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
import datetime



class Truck(models.Model):
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=50)


    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('truck_detail', kwargs={'truck_id': self.id})



class Menu(models.Model):
    food_name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    print(truck)

    def __str__(self):
        return self.food_name
    
    def get_absolute_url(self):
        return reverse('truck_detail', truck_id=truck_id)

class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    truck_owner = models.BooleanField(default=False)
    # choices=([('1', 'Yes'), ('2', 'No')])
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    

    trucks = models.ManyToManyField(Truck)

    def __str__(self):
        return self.user.username

class ProfilePhoto(models.Model):
    url = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for profile picture: {self.user_id} @ {self.url}"

class TruckPhoto(models.Model):
    url = models.CharField(max_length=200)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for truck picture: {self.truck_id} @ {self.url}"

class MenuPhoto(models.Model):
    url = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for menu picture: {self.menu_id} @ {self.url}"

class Calendar(models.Model):
    date = models.DateField()
    start_time = models.CharField(max_length=50)
    end_time = models.CharField(max_length=50)
    location = models.CharField(max_length=250)

    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date}, {self.time}, {self.location}'

    class Meta:
        ordering = ['-date']

class Review(models.Model):
    text = models.TextField(max_length=500)
    created_date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"{self.user.username} at {self.created_date}: {self.text}"

    class Meta:
        ordering = ['-created_date']


from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Truck(models.Model):
    name = models.CharField(max_length=50)
    style = models.CharField(max_length=50)


    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('truck_detail', kwargs={'pk': self.id})

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
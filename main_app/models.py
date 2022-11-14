from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


DETAILS = (
  ('R', 'Does not need maintenance'),
  ('M', 'Needs Further Maintenance'),
  ('O', 'Maintenance complete')
)

class Tires(models.Model):
  name = models.CharField(max_length=50)
  hardness = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('tires_detail', kwargs={'pk': self.id})

class Car(models.Model):
  name = models.CharField(max_length=100)
  make = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  year = models.IntegerField()
  tires = models.ManyToManyField(Tires)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('cars_detail', kwargs={'car_id': self.id})

  def maintenance_today(self):
    return self.maintenance_set.filter(date=date.today()).count() >= 1


class Maintenance(models.Model):
  date = models.DateField('Last Maintenance Date')
  details = models.CharField(
    max_length=1,
    choices = DETAILS,
    default= DETAILS[0][0]
  )

  car = models.ForeignKey(Car, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_details_display()} on {self.date}"

  class Meta:
    ordering = ['-date']


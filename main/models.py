from typing import Text
from django.db import models
from django.db.models.fields.related import ForeignKey, ForeignObject
from django.urls.conf import include
from django.utils import timezone
from django.db.models.fields import CharField, DateField, FloatField, IntegerField, TextField
from django.contrib.auth.models import User


class Children_Garden(models.Model):
    city=CharField(max_length=200)
    streat=CharField(max_length=200)
    name=CharField(max_length=200)
    capacity=IntegerField()
    def __str__(self) -> str:
        return self.name

class Educator(models.Model):
    first_name=CharField(max_length=200)
    last_name=CharField(max_length=200)
    age=IntegerField()
    gender=CharField(max_length=200)
    children_garden=ForeignKey(Children_Garden,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.first_name

class Parent(models.Model):
    first_name=CharField(max_length=200)
    last_name=CharField(max_length=200)
    age=IntegerField()
    gender=CharField(max_length=200)
    def __str__(self) -> str:
        return self.first_name

class Children(models.Model):
    first_name=CharField(max_length=200)
    last_name=CharField(max_length=200)
    age=IntegerField()
    gender=CharField(max_length=200)
    educator=ForeignKey(Educator,on_delete=models.CASCADE)
    parents=ForeignKey(Parent,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.first_name














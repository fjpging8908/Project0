from django.contrib.auth.models import User
from django.db import models
import  datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return  'Category:' + self.name

class Event(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='Category_Name')
    place = models.CharField(max_length=200, blank=True,null=True)
    address = models.CharField(max_length=200, blank=True,null=True)
    startDate = models.DateField(default=datetime.date.today)
    finishDate = models.DateField(default=datetime.date.today)
    eventType = models.CharField(max_length=2,choices=[('FF','face to face'),('VT','Virtual')],default='FF')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='User_Name',null=True)
    def __str__(self):
        return  'Event:' + self.name

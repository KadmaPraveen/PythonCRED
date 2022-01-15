
from django.db import models

# Create your models here.
class Position (models.Model) :
  title = models.CharField(max_length=50)

  #postion dropdown values not showing indropdown so below line code must include
  def __str__(self):
        return self.title

# class Employee(models.Model) :
# fullname=models.CharField(max_length=100)
# emp_code = models.charField(max_length=3)
# mobile = models.charField(max_length=3)
# position = models.ForeignKey(Position,on_delete=models.CASCADE)
#here give space for class and below fullname otherwise gets error.like below work above dnt work

class Employee(models.Model) :
    fullname=models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=3)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    
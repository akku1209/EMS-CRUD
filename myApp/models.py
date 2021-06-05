from django.db import models

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=50)
    esal=models.IntegerField()
    eaddr=models.CharField(max_length=50)

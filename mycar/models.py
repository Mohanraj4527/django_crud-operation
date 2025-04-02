from django.db import models

class myuser(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Phone=models.BigIntegerField()
    Email=models.EmailField()
    Model=models.CharField(max_length=20)
    Price=models.IntegerField()

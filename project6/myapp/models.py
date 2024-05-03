from django.db import models

# Create your models here.
class data(models.Model):
    Name=models.CharField(default="", max_length=50)
    Age=models.IntegerField(default="")
    Contact=models.IntegerField(default="")
    Mail=models.CharField(default="", max_length=50)

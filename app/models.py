from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Team(models.Model):

    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Driver(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    country = models.CharField(max_length=200)
    weight_before = models.FloatField(default=0)
    weight_after = models.FloatField(default=0, null=True)


    def __str__(self):
        return str(self.team)
    
class Race(models.Model):

    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    country = models.CharField(max_length=200)
    
    def __str__(self):
        return self.country 

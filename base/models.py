from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=10000)
    image = models.CharField(max_length=10000)
    speaker = models.CharField(max_length=10000)
    venue = models.CharField(max_length=10000)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name + self.speaker + self.venue
    
class YearGroup(models.Model):
    name = models.CharField(max_length=10000)

    def __str__(self):
        return self.name
    
class Ministry(models.Model):
    name = models.CharField(max_length=10000)

    def __str__(self):
        return self.name
    
class Registration(models.Model):
    fullname = models.CharField(max_length=10000)
    number = models.IntegerField()
    course = models.CharField(max_length=10000)
    year_group = models.ForeignKey(YearGroup, on_delete=models.CASCADE)
    ministry = models.ForeignKey(Ministry, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.fullname + self.number
from django.db import models
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class House(models.Model):
    name = models.CharField(max_length=100)
    rent = models.IntegerField()
    area = models.IntegerField(default=None)
    bedrooms = models.IntegerField(default=None)
    parking = models.BooleanField(default=False)
    img = models.ImageField(upload_to='images',default=None, )
    # img2 = models.ImageField(upload_to='images',default=None)
    # img3 = models.ImageField(upload_to='images',default=None)
    bathrooms = models.IntegerField(default=None)
    description = models.TextField(default="House")
    Owner = models.CharField(max_length= 100,default="Human")
    address = models.TextField(default="Earth")
    ListedByOwner = models.BooleanField(default=True)
    Type = models.CharField(max_length=20,default="Appartment")
    Publisher = models.ForeignKey(User,on_delete=models.CASCADE)



    def __str__(self):
        return self.name
from django.db import models
from datetime import datetime

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=15)
    discription = models.TextField()
    datetime = models.DateTimeField()  #  fix added here

    def __str__(self,):
        return self.name

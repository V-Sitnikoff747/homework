from django.db import models

class Restaurant(models.Model):

    name= models.CharField(max_length=50)
    address= models.CharField(max_length=90)
    specialization= models.TextField()
    website= models.URLField(blank= True)
    phone= models.CharField(max_length=25)

    def __str__(self):
        return self.name


from django.db import models



class Car(models.Model):
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100, null=False, db_index=True)
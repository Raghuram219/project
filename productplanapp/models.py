from django.db import models

class Products(models.Model):
    name=models.CharField(max_length=20)
    budget=models.IntegerField()
    
    def __str__(self):
        return self.name

class Plan(models.Model):
    plan=models.CharField(max_length=20)
    budget=models.IntegerField()
    products=models.ManyToManyField(Products)

    def __str__(self):
        return self.plan
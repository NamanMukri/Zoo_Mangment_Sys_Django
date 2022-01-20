from django.db import models

class Mammal(models.Model):
    name= models.CharField(max_length=20)
    species= models.CharField(max_length=20)
    gender= models.CharField(max_length=20)    
    food= models.CharField(max_length=20)
    last_feed_time= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
class Bird(models.Model):
    name= models.CharField(max_length=20)
    species= models.CharField(max_length=20)
    food= models.CharField(max_length=20)
    last_feed_time= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Fish(models.Model):
    color= models.CharField(max_length=20)
    species= models.CharField(max_length=20)
    food= models.CharField(max_length=20)
    count=models.IntegerField()
    last_feed_time= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.species
    


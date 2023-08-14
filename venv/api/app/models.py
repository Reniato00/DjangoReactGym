from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    isActive = models.BooleanField(default=False)
    createdAt= models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)
    validities = models.ManyToManyField('Validity', through='ClientValidity')
    
    def __str__(self):
        return self.name + ' ' + self.lastname + ' | Is Active: '+ str(self.isActive)
    
class Validity(models.Model):
    
    timeValidity = models.DateField()
    createdAt= models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    def __str__(self):
        return self.timeValidity
    
class ClientValidity(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    validity = models.ForeignKey(Validity, on_delete=models.CASCADE)
    createdAt= models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    def __str__(self):
        pass

class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    type = models.IntegerField(default=1)
    categories = models.ManyToManyField('CategoryPlace', through='PlaceCategoryPlace')
    createdAt= models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    def __str__(self):
        pass

class CategoryPlace(models.Model):
    name = models.CharField(max_length=100) # Only have 3 types of Gyms
    createdAt= models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    def __str__(self):
        pass

class PlaceCategoryPlace(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    categoryPlace = models.ForeignKey(CategoryPlace, on_delete=models.CASCADE)
    createdAt= models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    def __str__(self):
        pass

class Coach(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    age = models.IntegerField()
    createdAt= models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    def __str__(self):
        pass

class PlaceCoach(models.Model):
    place = models.ForeignKey(Place,related_name='coaches', on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach,related_name='places', on_delete=models.CASCADE)
    createdAt= models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    def __str__(self):
        pass






    



from django.db import models
from sqlalchemy import delete

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def save_location(self):
        self.save
    def delete_location(self):
        self.delete()
    def update_location(self,name):
        self.name
        self.save
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return self.name

class Photo(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    location=models.ForeignKey(Location, on_delete=models.CASCADE,null=True, blank=True)
    image=models.ImageField(null=False, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.description

from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def save_location(self):
        self.save()
    def delete_location(self):
        self.delete()
    def update_location(self,name):
        self.name
        self.save()
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def save_category(self):
        self.save()
    def delete_category(self):
        self.delete()
    def update_category(self,name):
        self.name
        self.save()
    def __str__(self):
        return self.name

class Photo(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    location=models.ForeignKey(Location, on_delete=models.CASCADE,null=True, blank=True)
    image=models.ImageField(null=False, blank=False)
    description = models.TextField()

    def save_image(self):
        self.save()
    def delete_image(self):
        self.delete()
    def update_image(self,name,description,image,location,category):
        self.name=name
        self.description=description
        self.image=image
        self.location=location
        self.category=category
        self.save()
    @classmethod
    def get_image_by_id(cls,my_id):
        output=cls.objects.get(id=my_id)
        return output
    @classmethod
    def search_images(cls,category):
        image_output=cls.objects.filter(category__name=category)
        return image_output
    @classmethod
    def search_by_category(cls,search_term):
        photos=cls.objects.filter(category__name=search_term)
        return photos
    @classmethod
    def filter_by_location(cls,location):
        image_output2=cls.objects.filter(location__name=location)
        return image_output2
   
    def __str__(self):
        return self.description

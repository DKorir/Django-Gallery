from re import L
from unicodedata import category
from django.test import TestCase

# Create your tests here.
from .models import Photo,Location,Category
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kisumu= Location(name = 'kisumu',)
    def test_instance(self):
        self.assertTrue(isinstance(self.kisumu,Location))
    def test_save_method(self):
        self.kisumu.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)
    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Photo.objects.all().delete()

class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.technology= Category(name = 'kisumu',)
    def test_instance(self):
        self.assertTrue(isinstance(self.technology,Category))
    def test_save_method(self):
        self.technology.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)


class PhotoTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.photo= Photo(image ='Muriuki', description ='kenya is lovely country')
    def test_instance(self):
        self.assertTrue(isinstance(self.photo,Photo))
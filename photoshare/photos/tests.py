from re import L
from django.test import TestCase

# Create your tests here.
from .models import Photo,Location,Category
class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.kisumu= Location(name = 'kisumu',)
    def test_instance(self):
        self.assertTrue(isinstance(self.kisumu,Location))
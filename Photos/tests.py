from django.test import TestCase

from .models import Category

# Create your tests here.
class CategoryTest(TestCase):

    def test_create(self):
        category = Category(name="Test Category")

        # test __str__ method
        self.assertEqual(str(category), "Test Category")

        # name 
        self.assertEqual(category.name, "Test Category")
from django.test import TestCase
from django.db.utils import IntegrityError
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Category, Photo

import os

# Create your tests here.
class TestCategories(TestCase):

    def test_category_str_method(self):
        category_object = Category.objects.create(name="Nature")

        self.assertEqual(str(category_object), "Nature")
    
    def test_category_unique(self):
        with self.assertRaises(IntegrityError) as raised:
            Category.objects.create(name="Nature")
            Category.objects.create(name="Nature")

        self.assertEqual(IntegrityError, type(raised.exception))

class TestPhoto(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Nature")
    
    def tearDown(self):

        if hasattr(self, 'photo_object'):
            image_path = self.photo_object.image.path

            print("Removing image..", image_path)
            if os.path.exists(image_path):
                os.remove(image_path)

    def test_upload_photo(self):
        self.photo_object = Photo.objects.create(
            name = 'Forest Photo',
            category = self.category,
            image = SimpleUploadedFile(name="test_image.jpg", content=open('E:/tmp/big-one.jpg', 'rb').read(), content_type='image/jpg'),
            description = "Test description"
        )

        self.assertTrue(os.path.exists(self.photo_object.image.path))
    
    def test_delete_photo(self):
        photo_object = Photo.objects.create(
            name = 'Forest Photo',
            category = self.category,
            image = SimpleUploadedFile(name="test_image.jpg", content=open('E:/tmp/big-one.jpg', 'rb').read(), content_type='image/jpg'),
            description = "Test description"
        )

        self.assertTrue(os.path.exists(photo_object.image.path))

        photo_object.delete()

        self.assertFalse(os.path.exists(photo_object.image.path))
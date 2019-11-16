from django.test import TestCase, SimpleTestCase

from .forms import ContactForm

# Create your tests here.
class TestPages(TestCase):
    
    def test_home_page_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_about_page_status(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
    
    def test_contact_page_status(self):
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_home_conext(self):
        """
        Tests if home gets photos in context
        """
        response = self.client.get('/')
        self.assertIsNotNone(response.context.get("photos"))

class ContactTest(TestCase):
    def test_valid_form(self):
        form_data = {
            "name" : "Test User",
            "email" : "test@mail.com",
            "message" : "test message"
        }

        form = ContactForm(form_data)

        self.assertTrue(form.is_valid())
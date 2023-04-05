from django.test import TestCase,Client
from django.urls import reverse

class HelloViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
    def test_hello(self):
        response = self.client.get(reverse("hello-view"))
        excepted_data = "Hello" 
        self.assertEqual(excepted_data,response.content.decode())  
        self.assertEqual(500,response.status_code)
        self.assertEqual(response['name'],'alex')

    def test_about(self):
        response = self.client.get(reverse("about-view"))
        excepted_data = "white" 
        self.assertEqual(excepted_data,response.content.decode())  

    def test_contacts(self):
        response = self.client.get(reverse("contacts-view"))
        excepted_data = "black" 
        self.assertEqual(excepted_data,response.content.decode())  
       
